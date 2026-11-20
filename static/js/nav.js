// The sidebar: which signed-in screen is showing.
//
// Every screen is a <section class="view" data-view="name" data-path="/area/name">
// in index.html, and a sidebar link to that path. The URL's path is the only
// state -- back, forward, reload and a pasted link all land on the same
// screen. The server serves index.html for exactly the paths index.html
// declares (static_files.py reads them), so a reload works and any other path
// is still a real 404.
//
// A screen marked data-subpaths also owns every path under its own: the
// Process screen's /ais/<id>-<folder>/<image> and the Batches screen's
// /batches/folder/<id>. The screen reads the rest itself (ais.js,
// batch_folders.js), and the server has a route for each (routes/__init__.py).
//
// A card can have a path too (/account/two-factor, /about/measures): that
// opens the screen it is on and scrolls to it. Links from before screens had
// paths (#users, #two-factor, #ais/3-folder/image) are turned into their path
// on load, so old bookmarks work.
//
// Whether a screen exists for this user is not decided here. The screen's own
// file un-hides its section (Keys.init shows the All API keys screen, and only
// if the server has them switched on); Nav only offers what was un-hidden. So
// app.js calls Nav.init() last, once every screen has had its say.
//
// After every change of screen, and every Back or Forward, Nav sends a "nav"
// event on window, which is how a screen hears it was opened or that its part
// of the path changed.
const Nav = {
  fallback: "ais",
  // Matches Bootstrap's lg breakpoint, where offcanvas-lg becomes a column.
  wide: window.matchMedia( "(min-width: 992px)" ),
  // Collapsed-or-not is a per-browser convenience, like the theme.
  storageKey: "sidebar-collapsed",
  // Old hash links to screens that are now cards on Account: hash -> card id.
  moved: {
    "password": "password-panel",
    "pin": "pin-panel",
    "two-factor": "two-factor-panel",
    "api-keys": "api-keys-panel",
  },

  init() {
    Dom.all( "[data-nav]" ).forEach( ( link ) => {
      Dom.show( link , this.available( link.getAttribute( "data-nav" ) ) );
      link.addEventListener( "click" , () => this.closeSidebar() );
    } );
    // A group heading with nothing left under it goes too.
    Dom.all( ".sidebar-group" ).forEach( function ( group ) {
      Dom.show( group , Dom.all( "[data-nav]:not([hidden])" , group ).length > 0 );
    } );
    // Before the sidebar appears, so a collapsed one never flashes open.
    this.setCollapsed( this.savedCollapsed() );
    Dom.show( Dom.get( "sidebar" ) , true );
    const toggle = Dom.get( "sidebar-toggle" );
    toggle.addEventListener( "click" , () => this.toggleSidebar() );
    Dom.show( toggle , true );

    // Any link to a screen's or card's path changes screen without a page
    // load: the sidebar, links inside screens, a Batches folder tile.
    document.addEventListener( "click" , ( event ) => this.follow( event ) );
    // Moving between screens is not an undo step: Back and Forward already
    // are that, and an undo that only changed the screen would get in the way
    // of undoing what was done on it.
    // With a newer build waiting, the switch is a page load instead (fresh.js).
    window.addEventListener( "popstate" , () => {
      if ( !Fresh.swap() ) this.render();
    } );
    this.adoptHash();
    this.render();
  },

  // A plain click on a link to a path this page shows. A new tab, a
  // download, or a path that is not a screen here is left to the browser.
  follow( event ) {
    if ( event.defaultPrevented || event.button !== 0 ) return;
    if ( event.metaKey || event.ctrlKey || event.shiftKey || event.altKey ) return;
    const link = event.target.closest ? event.target.closest( "a[href^='/']" ) : null;
    if ( !link || link.target || link.hasAttribute( "download" ) ) return;
    const path = this.clean( link.getAttribute( "href" ) );
    if ( !this.find( path ) ) return;
    event.preventDefault();
    this.go( path );
  },

  // Undo uses this to go back to the screen an action happened on.
  show( name ) {
    this.go( this.pathOf( name ) );
  },

  go( path ) {
    if ( path !== this.clean( window.location.pathname ) ) window.history.pushState( null , "" , path );
    if ( !Fresh.swap() ) this.render();
  },

  available( name ) {
    const view = document.querySelector( '.view[data-view="' + name + '"]' );
    return Boolean( view ) && !view.hidden;
  },

  pathOf( name ) {
    const view = document.querySelector( '.view[data-view="' + name + '"]' );
    return view ? view.getAttribute( "data-path" ) : "/";
  },

  // "/admin/users/" and "/admin/users" are the same screen.
  clean( path ) {
    return path.replace( /[?#].*$/ , "" ).replace( /\/+$/ , "" ) || "/";
  },

  // The screen (and card, if the path names one) a path opens, when this user
  // has that screen and the card is showing. null for anything else. A path
  // under a data-subpaths screen's own opens that screen.
  find( path ) {
    let node = Dom.all( "[data-path]" ).find( ( each ) => each.getAttribute( "data-path" ) === path );
    if ( !node ) {
      node = Dom.all( ".view[data-subpaths]" ).find( ( view ) => path.startsWith( view.getAttribute( "data-path" ) + "/" ) );
    }
    const view = node && node.closest( ".view" );
    if ( !view || !this.available( view.getAttribute( "data-view" ) ) ) return null;
    if ( node !== view && node.hidden ) return null;
    return { name: view.getAttribute( "data-view" ) , card: node === view ? null : node };
  },

  // A path naming a screen this user does not have (an admin link opened by a
  // non-admin, a typo, or just "/") shows the Process screen rather than nothing.
  current() {
    const found = this.find( this.clean( window.location.pathname ) );
    return found ? found.name : this.fallback;
  },

  // A link from before screens had paths: #users, #two-factor,
  // #two-factor-panel, #ais/3-folder/image, #batches/folder/12. Swapped for
  // the path, in place, so Back does not return to it.
  adoptHash() {
    const old = window.location.hash.replace( /^#/ , "" );
    if ( old === "" ) return;
    const first = old.split( "/" )[ 0 ];
    const rest = old.slice( first.length );
    const id = Object.prototype.hasOwnProperty.call( this.moved , first ) ? this.moved[ first ] : first;
    const view = document.querySelector( '.view[data-view="' + CSS.escape( first ) + '"]' );
    const node = view || document.getElementById( id );
    let path = node && node.getAttribute( "data-path" );
    if ( path && rest !== "" ) path = view && view.hasAttribute( "data-subpaths" ) ? path + rest : null;
    if ( path ) window.history.replaceState( null , "" , path );
  },

  render() {
    const found = this.find( this.clean( window.location.pathname ) );
    const name = found ? found.name : this.fallback;
    // The address bar says where they are, also after "/" or an unknown path.
    if ( !found ) window.history.replaceState( null , "" , this.pathOf( name ) );
    Track.nav( name );
    Dom.all( ".view" ).forEach( function ( view ) {
      view.classList.toggle( "view-active" , view.getAttribute( "data-view" ) === name );
    } );
    Dom.all( "[data-nav]" ).forEach( function ( link ) {
      const active = link.getAttribute( "data-nav" ) === name;
      link.classList.toggle( "active" , active );
      if ( active ) link.setAttribute( "aria-current" , "page" );
      else link.removeAttribute( "aria-current" );
    } );
    if ( found && found.card ) Dom.reveal( found.card , "start" );
    else {
      Dom.movedOnPurpose();
      window.scrollTo( 0 , 0 );
    }
    this.announce( name );
    window.dispatchEvent( new CustomEvent( "nav" , { detail: { screen: name } } ) );
  },

  // Changing screen reloads nothing, so nothing tells a screen reader or the
  // browser's tab that anything happened. The title names the screen, and the
  // focus moves to its heading, except on load, when it belongs to the page.
  announce( name ) {
    const heading = document.querySelector( '.view[data-view="' + name + '"] h2' );
    if ( !heading ) return;
    const title = I18n.get( "nav.page_title" );
    // The Process screen's h2 is the open image's name, empty until there is
    // one, so its sidebar entry names it instead.
    const link = document.querySelector( '#sidebar-nav [data-nav="' + name + '"]' );
    const screen = heading.textContent.trim() || ( link ? link.textContent.trim() : "" );
    if ( title !== "" ) document.title = title.replace( "{screen}" , () => screen ).replace( "{app}" , () => I18n.get( "app.title" ) );
    const moved = this.shown !== undefined && this.shown !== name;
    this.shown = name;
    if ( !moved ) return;
    heading.setAttribute( "tabindex" , "-1" );
    heading.focus( { preventScroll: true } );
  },

  // The menu button: on a wide screen it folds the sidebar column away and
  // back; on a phone it slides the panel in and out. Only the folding is
  // undoable: the phone panel is gone again as soon as a screen is picked.
  toggleSidebar() {
    if ( this.wide.matches ) {
      const collapsed = !document.documentElement.classList.contains( "sidebar-collapsed" );
      Undo.run( {
        label: I18n.get( "undo.sidebar" ),
        screen: null,
        do: () => this.saveCollapsed( collapsed ),
        undo: () => this.saveCollapsed( !collapsed ),
      } );
    } else if ( window.bootstrap ) {
      bootstrap.Offcanvas.getOrCreateInstance( Dom.get( "sidebar" ) ).toggle();
    }
  },

  setCollapsed( collapsed ) {
    document.documentElement.classList.toggle( "sidebar-collapsed" , collapsed );
    Dom.get( "sidebar-toggle" ).setAttribute( "aria-expanded" , String( !collapsed ) );
  },

  saveCollapsed( collapsed ) {
    this.setCollapsed( collapsed );
    try {
      if ( collapsed ) window.localStorage.setItem( this.storageKey , "1" );
      else window.localStorage.removeItem( this.storageKey );
    } catch ( error ) { /* storage blocked: it just is not remembered */ }
  },

  savedCollapsed() {
    try {
      return window.localStorage.getItem( this.storageKey ) === "1";
    } catch ( error ) {
      return false;
    }
  },

  // On a phone the sidebar is a slide-in panel; picking a screen closes it,
  // including the one already showing.
  closeSidebar() {
    const panel = window.bootstrap && bootstrap.Offcanvas.getInstance( Dom.get( "sidebar" ) );
    if ( panel ) panel.hide();
  },
};
