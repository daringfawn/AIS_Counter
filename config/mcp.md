# AIS Counter MCP tools

This file is generated: do not edit it. Change the tools next to their handlers and run `scripts/api_docs.sh`. Every route is in [api.md](api.md).

Every tool POST /mcp offers. Written by scripts/api_docs.sh from the registered tools; do not edit by hand. A key sees the tools its role allows (adminOnly ones need an admin key), and a tool whose feature is switched off answers like one that does not exist. route is the HTTP route the tool stands for, with the same rules; http_only are the routes a key may call that have no tool, and why.

|  |  |
|---|---|
| Endpoint | `POST /mcp` |
| Transport | Streamable HTTP, stateless: one JSON-RPC message per POST, a JSON reply |
| Auth | Authorization: Bearer <API key> |

| Tool | Route | Who | What |
|---|---|---|---|
| [`admin_cancel_login_link`](#admin_cancel_login_link) | [`POST /api/admin/users/{user_id}/cancel-login-link`](api.md#post-apiadminusersuser_idcancel-login-link) | admin keys | Stop an account's login link working (admin) |
| [`admin_cancel_login_link_bulk`](#admin_cancel_login_link_bulk) | [`POST /api/bulk/admin/users/cancel-login-link`](api.md#post-apibulkadminuserscancel-login-link) | admin keys | Stop an account's login link working, for many at once (admin) |
| [`admin_create_invite_link`](#admin_create_invite_link) | [`POST /api/admin/invite-links`](api.md#post-apiadmininvite-links) | admin keys | Create an invite link (admin) |
| [`admin_create_user`](#admin_create_user) | [`POST /api/admin/users`](api.md#post-apiadminusers) | admin keys | Create an account (admin) |
| [`admin_delete_invite_link`](#admin_delete_invite_link) | [`POST /api/admin/invite-links/{link_id}/delete`](api.md#post-apiadmininvite-linkslink_iddelete) | admin keys | Delete an invite link (admin) |
| [`admin_delete_invite_link_bulk`](#admin_delete_invite_link_bulk) | [`POST /api/bulk/admin/invite-links/delete`](api.md#post-apibulkadmininvite-linksdelete) | admin keys | Delete an invite link, for many at once (admin) |
| [`admin_delete_user`](#admin_delete_user) | [`POST /api/admin/users/{user_id}/delete`](api.md#post-apiadminusersuser_iddelete) | admin keys | Delete an account (admin) |
| [`admin_delete_user_bulk`](#admin_delete_user_bulk) | [`POST /api/bulk/admin/users/delete`](api.md#post-apibulkadminusersdelete) | admin keys | Delete an account, for many at once (admin) |
| [`admin_get_theme_defaults`](#admin_get_theme_defaults) | [`GET /api/admin/theme-defaults`](api.md#get-apiadmintheme-defaults) | admin keys | Default themes (admin) |
| [`admin_list_invite_links`](#admin_list_invite_links) | [`GET /api/admin/invite-links`](api.md#get-apiadmininvite-links) | admin keys | List invite links (admin) |
| [`admin_list_user_sessions`](#admin_list_user_sessions) | [`GET /api/admin/users/{user_id}/sessions`](api.md#get-apiadminusersuser_idsessions) | admin keys | An account's signed-in devices (admin) |
| [`admin_list_users`](#admin_list_users) | [`GET /api/admin/users`](api.md#get-apiadminusers) | admin keys | List users (admin) |
| [`admin_reissue_login`](#admin_reissue_login) | [`POST /api/admin/users/{user_id}/reissue-login`](api.md#post-apiadminusersuser_idreissue-login) | admin keys | A new login link for an account (admin) |
| [`admin_rename_invite_link`](#admin_rename_invite_link) | [`POST /api/admin/invite-links/{link_id}/rename`](api.md#post-apiadmininvite-linkslink_idrename) | admin keys | Rename an invite link (admin) |
| [`admin_rename_user`](#admin_rename_user) | [`POST /api/admin/users/{user_id}/rename`](api.md#post-apiadminusersuser_idrename) | admin keys | Rename someone (admin) |
| [`admin_reset_two_factor`](#admin_reset_two_factor) | [`POST /api/admin/users/{user_id}/reset-two-factor`](api.md#post-apiadminusersuser_idreset-two-factor) | admin keys | Turn off an account's two-factor (admin) |
| [`admin_reset_two_factor_bulk`](#admin_reset_two_factor_bulk) | [`POST /api/bulk/admin/users/reset-two-factor`](api.md#post-apibulkadminusersreset-two-factor) | admin keys | Turn off an account's two-factor, for many at once (admin) |
| [`admin_restore_invite_link`](#admin_restore_invite_link) | [`POST /api/admin/invite-links/{link_id}/restore`](api.md#post-apiadmininvite-linkslink_idrestore) | admin keys | Undo deleting an invite link (admin) |
| [`admin_restore_invite_link_bulk`](#admin_restore_invite_link_bulk) | [`POST /api/bulk/admin/invite-links/restore`](api.md#post-apibulkadmininvite-linksrestore) | admin keys | Undo deleting an invite link, for many at once (admin) |
| [`admin_revoke_access`](#admin_revoke_access) | [`POST /api/admin/users/{user_id}/revoke-access`](api.md#post-apiadminusersuser_idrevoke-access) | admin keys | Revoke a user's access (admin) |
| [`admin_revoke_access_bulk`](#admin_revoke_access_bulk) | [`POST /api/bulk/admin/users/revoke-access`](api.md#post-apibulkadminusersrevoke-access) | admin keys | Revoke a user's access, for many at once (admin) |
| [`admin_revoke_invite_link`](#admin_revoke_invite_link) | [`POST /api/admin/invite-links/{link_id}/revoke`](api.md#post-apiadmininvite-linkslink_idrevoke) | admin keys | Switch off an invite link (admin) |
| [`admin_revoke_invite_link_bulk`](#admin_revoke_invite_link_bulk) | [`POST /api/bulk/admin/invite-links/revoke`](api.md#post-apibulkadmininvite-linksrevoke) | admin keys | Switch off an invite link, for many at once (admin) |
| [`admin_revoke_user_session`](#admin_revoke_user_session) | [`POST /api/admin/users/{user_id}/sessions/{session_id}/revoke`](api.md#post-apiadminusersuser_idsessionssession_idrevoke) | admin keys | Sign out one of an account's devices (admin) |
| [`admin_revoke_user_session_bulk`](#admin_revoke_user_session_bulk) | [`POST /api/bulk/admin/users/sessions/revoke`](api.md#post-apibulkadminuserssessionsrevoke) | admin keys | Sign out one of an account's devices, for many at once (admin) |
| [`admin_set_invite_link_limits`](#admin_set_invite_link_limits) | [`POST /api/admin/invite-links/{link_id}/limits`](api.md#post-apiadmininvite-linkslink_idlimits) | admin keys | Change an invite link's places and expiry (admin) |
| [`admin_set_theme_defaults`](#admin_set_theme_defaults) | [`POST /api/admin/theme-defaults`](api.md#post-apiadmintheme-defaults) | admin keys | Replace the default themes (admin) |
| [`admin_set_user_disabled`](#admin_set_user_disabled) | [`POST /api/admin/users/{user_id}/disabled`](api.md#post-apiadminusersuser_iddisabled) | admin keys | Disable or enable a user (admin) |
| [`admin_set_user_disabled_bulk`](#admin_set_user_disabled_bulk) | [`POST /api/bulk/admin/users/disabled`](api.md#post-apibulkadminusersdisabled) | admin keys | Disable or enable a user, for many at once (admin) |
| [`admin_set_user_expiry`](#admin_set_user_expiry) | [`POST /api/admin/users/{user_id}/expiry`](api.md#post-apiadminusersuser_idexpiry) | admin keys | Set when an account expires (admin) |
| [`admin_set_user_role`](#admin_set_user_role) | [`POST /api/admin/users/{user_id}/role`](api.md#post-apiadminusersuser_idrole) | admin keys | Change an account's role (admin) |
| [`admin_set_user_role_bulk`](#admin_set_user_role_bulk) | [`POST /api/bulk/admin/users/role`](api.md#post-apibulkadminusersrole) | admin keys | Change an account's role, for many at once (admin) |
| [`admin_switch_on_invite_link`](#admin_switch_on_invite_link) | [`POST /api/admin/invite-links/{link_id}/switch-on`](api.md#post-apiadmininvite-linkslink_idswitch-on) | admin keys | Switch an invite link back on (admin) |
| [`admin_switch_on_invite_link_bulk`](#admin_switch_on_invite_link_bulk) | [`POST /api/bulk/admin/invite-links/switch-on`](api.md#post-apibulkadmininvite-linksswitch-on) | admin keys | Switch an invite link back on, for many at once (admin) |
| [`cancel_my_login_link`](#cancel_my_login_link) | [`POST /api/account/login-link/cancel`](api.md#post-apiaccountlogin-linkcancel) | any key | Stop your own login link working |
| [`create_my_login_link`](#create_my_login_link) | [`POST /api/account/login-link`](api.md#post-apiaccountlogin-link) | any key | A login link for yourself |
| [`label_my_session`](#label_my_session) | [`POST /api/account/sessions/{session_id}/label`](api.md#post-apiaccountsessionssession_idlabel) | any key | Name one of your devices |
| [`list_my_sessions`](#list_my_sessions) | [`GET /api/account/sessions`](api.md#get-apiaccountsessions) | any key | Your signed-in devices |
| [`list_team`](#list_team) | [`GET /api/team`](api.md#get-apiteam) | any key | List team |
| [`rename_account`](#rename_account) | [`POST /api/account/rename`](api.md#post-apiaccountrename) | any key | Rename your account |
| [`revoke_my_other_sessions`](#revoke_my_other_sessions) | [`POST /api/account/sessions/revoke-others`](api.md#post-apiaccountsessionsrevoke-others) | any key | Sign out all your devices |
| [`revoke_my_session`](#revoke_my_session) | [`POST /api/account/sessions/{session_id}/revoke`](api.md#post-apiaccountsessionssession_idrevoke) | any key | Sign out one of your devices |
| [`revoke_my_session_bulk`](#revoke_my_session_bulk) | [`POST /api/bulk/account/sessions/revoke`](api.md#post-apibulkaccountsessionsrevoke) | any key | Sign out one of your devices, for many at once |
| [`set_shortcuts`](#set_shortcuts) | [`POST /api/account/shortcuts`](api.md#post-apiaccountshortcuts) | any key | Set your keyboard shortcuts |
| [`set_theme`](#set_theme) | [`POST /api/account/theme`](api.md#post-apiaccounttheme) | any key | Pick your theme |
| [`set_themes`](#set_themes) | [`POST /api/account/themes`](api.md#post-apiaccountthemes) | any key | Replace your own themes |
| [`whoami`](#whoami) | [`GET /api/me`](api.md#get-apime) | any key | Who am I |
| [`list_batches`](#list_batches) | [`GET /api/ais/batches`](api.md#get-apiaisbatches) | any key | List batches |
| [`list_folders`](#list_folders) | [`GET /api/ais/folders`](api.md#get-apiaisfolders) | any key | List folders |
| [`get_batch`](#get_batch) | [`GET /api/ais/batches/{batch_id}`](api.md#get-apiaisbatchesbatch_id) | any key | Get a batch |
| [`batch_status`](#batch_status) | [`GET /api/ais/batches/{batch_id}/status`](api.md#get-apiaisbatchesbatch_idstatus) | any key | Batch image status |
| [`batch_channels`](#batch_channels) | [`GET /api/ais/batches/{batch_id}/channels`](api.md#get-apiaisbatchesbatch_idchannels) | any key | Batch .czi channels |
| [`list_results`](#list_results) | [`GET /api/ais/results`](api.md#get-apiaisresults) | any key | List results |
| [`list_measurements`](#list_measurements) | [`GET /api/ais/measurements`](api.md#get-apiaismeasurements) | any key | List recorded lines |
| [`list_measure_types`](#list_measure_types) | [`GET /api/ais/measure-types`](api.md#get-apiaismeasure-types) | any key | List measurement types |
| [`create_batch`](#create_batch) | [`POST /api/ais/batches`](api.md#post-apiaisbatches) | any key | Create an empty batch |
| [`create_batch_from_files`](#create_batch_from_files) | [`POST /api/ais/batches/upload`](api.md#post-apiaisbatchesupload) | any key | Create a batch from files |
| [`add_files_to_batch`](#add_files_to_batch) | [`POST /api/ais/batches/{batch_id}/upload`](api.md#post-apiaisbatchesbatch_idupload) | any key | Add files to a batch |
| [`get_channel_layouts`](#get_channel_layouts) | [`GET /api/ais/batches/{batch_id}/layouts`](api.md#get-apiaisbatchesbatch_idlayouts) | any key | List a batch's channel layouts |
| [`set_channel_roles`](#set_channel_roles) | [`POST /api/ais/batches/{batch_id}/layouts`](api.md#post-apiaisbatchesbatch_idlayouts) | any key | Set channel roles |
| [`fill_missing_areas`](#fill_missing_areas) | [`POST /api/ais/batches/{batch_id}/fill-areas`](api.md#post-apiaisbatchesbatch_idfill-areas) | any key | Fill in missing AIS areas |
| [`rename_batch`](#rename_batch) | [`POST /api/ais/batches/{batch_id}/rename`](api.md#post-apiaisbatchesbatch_idrename) | any key | Rename a batch |
| [`archive_batch`](#archive_batch) | [`POST /api/ais/batches/{batch_id}/archive`](api.md#post-apiaisbatchesbatch_idarchive) | any key | Archive or bring back a batch |
| [`set_images_included`](#set_images_included) | [`POST /api/ais/batches/{batch_id}/include`](api.md#post-apiaisbatchesbatch_idinclude) | any key | Include or leave out images |
| [`set_image_done`](#set_image_done) | [`POST /api/ais/batches/{batch_id}/done`](api.md#post-apiaisbatchesbatch_iddone) | any key | Mark an image done |
| [`assign_batch`](#assign_batch) | [`POST /api/ais/batches/{batch_id}/assign`](api.md#post-apiaisbatchesbatch_idassign) | admin keys | Assign a batch (admin) |
| [`order_batches`](#order_batches) | [`POST /api/ais/batches/order`](api.md#post-apiaisbatchesorder) | admin keys | Order batches (admin) |
| [`move_batches`](#move_batches) | [`POST /api/ais/batches/move`](api.md#post-apiaisbatchesmove) | admin keys | Move batches into a folder (admin) |
| [`create_folder`](#create_folder) | [`POST /api/ais/folders`](api.md#post-apiaisfolders) | admin keys | Create a folder (admin) |
| [`rename_folder`](#rename_folder) | [`POST /api/ais/folders/{folder_id}/rename`](api.md#post-apiaisfoldersfolder_idrename) | admin keys | Rename a folder (admin) |
| [`move_folder`](#move_folder) | [`POST /api/ais/folders/{folder_id}/move`](api.md#post-apiaisfoldersfolder_idmove) | admin keys | Move a folder (admin) |
| [`order_folders`](#order_folders) | [`POST /api/ais/folders/order`](api.md#post-apiaisfoldersorder) | admin keys | Order folders (admin) |
| [`get_treatments`](#get_treatments) | [`GET /api/ais/batches/{batch_id}/treatments`](api.md#get-apiaisbatchesbatch_idtreatments) | admin keys | Get treatments (admin) |
| [`set_treatments`](#set_treatments) | [`POST /api/ais/batches/{batch_id}/treatments`](api.md#post-apiaisbatchesbatch_idtreatments) | admin keys | Set treatments (admin) |
| [`get_translation`](#get_translation) | [`GET /api/ais/batches/{batch_id}/translation.txt`](api.md#get-apiaisbatchesbatch_idtranslationtxt) | admin keys | Get __Translation.txt (admin) |
| [`load_translation`](#load_translation) | [`POST /api/ais/batches/{batch_id}/translation`](api.md#post-apiaisbatchesbatch_idtranslation) | admin keys | Load a __Translation.txt (admin) |
| [`rerandomize_add`](#rerandomize_add) | [`POST /api/ais/batches/{batch_id}/adds/{add_id}/randomize`](api.md#post-apiaisbatchesbatch_idaddsadd_idrandomize) | admin keys | New random names for a folder (admin) |
| [`get_backup`](#get_backup) | [`GET /api/ais/batches/{batch_id}/backup`](api.md#get-apiaisbatchesbatch_idbackup) | admin keys | Back up a batch (admin) |
| [`save_result`](#save_result) | [`POST /api/ais/results`](api.md#post-apiaisresults) | any key | Save an AIS |
| [`update_result`](#update_result) | [`POST /api/ais/results/{result_id}/update`](api.md#post-apiaisresultsresult_idupdate) | any key | Change an AIS |
| [`set_result_soma`](#set_result_soma) | [`POST /api/ais/results/{result_id}/soma`](api.md#post-apiaisresultsresult_idsoma) | any key | Set an AIS's soma distance |
| [`delete_result`](#delete_result) | [`POST /api/ais/results/{result_id}/delete`](api.md#post-apiaisresultsresult_iddelete) | any key | Delete an AIS |
| [`add_measurement`](#add_measurement) | [`POST /api/ais/measurements`](api.md#post-apiaismeasurements) | any key | Record a line |
| [`update_measurement`](#update_measurement) | [`POST /api/ais/measurements/{measurement_id}/update`](api.md#post-apiaismeasurementsmeasurement_idupdate) | any key | Change a recorded line |
| [`delete_measurement`](#delete_measurement) | [`POST /api/ais/measurements/{measurement_id}/delete`](api.md#post-apiaismeasurementsmeasurement_iddelete) | any key | Delete a recorded line |
| [`set_measure_types`](#set_measure_types) | [`POST /api/ais/measure-types`](api.md#post-apiaismeasure-types) | admin keys | Set measurement types (admin) |
| [`reset_batch_auto`](#reset_batch_auto) | [`POST /api/ais/batches/{batch_id}/reset`](api.md#post-apiaisbatchesbatch_idreset) | admin keys | Delete a batch's auto AIS (admin) |
| [`auto_defaults`](#auto_defaults) | [`GET /api/ais/auto/defaults`](api.md#get-apiaisautodefaults) | any key | Auto mode defaults |
| [`start_auto_run`](#start_auto_run) | [`POST /api/ais/batches/{batch_id}/auto`](api.md#post-apiaisbatchesbatch_idauto) | any key | Start an auto run |
| [`get_auto_run`](#get_auto_run) | [`GET /api/ais/auto/{run_id}`](api.md#get-apiaisautorun_id) | any key | Auto run status |
| [`list_auto_runs`](#list_auto_runs) | [`GET /api/ais/auto`](api.md#get-apiaisauto) | any key | List auto runs |
| [`cancel_auto_run`](#cancel_auto_run) | [`POST /api/ais/auto/{run_id}/cancel`](api.md#post-apiaisautorun_idcancel) | any key | Stop an auto run |
| [`export_report`](#export_report) | [`GET /api/ais/report`](api.md#get-apiaisreport) | any key | Export a report as JSON |
| [`compare_batches`](#compare_batches) | [`POST /api/ais/compare`](api.md#post-apiaiscompare) | admin keys | Compare batches by treatment (admin) |
| [`archive_batch_bulk`](#archive_batch_bulk) | [`POST /api/bulk/ais/batches/archive`](api.md#post-apibulkaisbatchesarchive) | any key | Archive or bring back a batch, for many at once |
| [`set_image_done_bulk`](#set_image_done_bulk) | [`POST /api/bulk/ais/batches/done`](api.md#post-apibulkaisbatchesdone) | any key | Mark an image done, for many at once |
| [`assign_batch_bulk`](#assign_batch_bulk) | [`POST /api/bulk/ais/batches/assign`](api.md#post-apibulkaisbatchesassign) | admin keys | Assign a batch (admin), for many at once |
| [`update_result_bulk`](#update_result_bulk) | [`POST /api/bulk/ais/results/update`](api.md#post-apibulkaisresultsupdate) | any key | Change an AIS, for many at once |
| [`delete_result_bulk`](#delete_result_bulk) | [`POST /api/bulk/ais/results/delete`](api.md#post-apibulkaisresultsdelete) | any key | Delete an AIS, for many at once |
| [`update_measurement_bulk`](#update_measurement_bulk) | [`POST /api/bulk/ais/measurements/update`](api.md#post-apibulkaismeasurementsupdate) | any key | Change a recorded line, for many at once |
| [`delete_measurement_bulk`](#delete_measurement_bulk) | [`POST /api/bulk/ais/measurements/delete`](api.md#post-apibulkaismeasurementsdelete) | any key | Delete a recorded line, for many at once |
| [`upload_instructions`](#upload_instructions) | [`POST /api/ais/files`](api.md#post-apiaisfiles) | any key | How to upload files |
| [`files_stored`](#files_stored) | [`POST /api/ais/files`](api.md#post-apiaisfiles) | any key | Which files the server has |
| [`get_image`](#get_image) | [`GET /api/ais/files/{sha}/view.png`](api.md#get-apiaisfilesshaviewpng) | any key | Look at an image |
| [`trace_click`](#trace_click) | [`POST /api/ais/trace`](api.md#post-apiaistrace) | any key | Trace an AIS from a click |
| [`detect_image`](#detect_image) | [`POST /api/ais/detect`](api.md#post-apiaisdetect) | any key | Find AIS on one image |

## admin_cancel_login_link

Void an account's live login link without making a new one: a link that went somewhere it should not have. Devices it already signed in stay signed in; admin_revoke_access ends those too. Answers with removed: 0 or 1.

|  |  |
|---|---|
| Route | [`POST /api/admin/users/{user_id}/cancel-login-link`](api.md#post-apiadminusersuser_idcancel-login-link) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |

## admin_cancel_login_link_bulk

Runs admin_cancel_login_link once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/admin/users/cancel-login-link`](api.md#post-apibulkadminuserscancel-login-link) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |

## admin_create_invite_link

One link for a group: each person who opens it joins as a new account with role (user, the default, or viewer), up to max_uses people, for days days. Answers with join_url (shown only now) and the link's details. Revoking or deleting this API key switches the link off.

|  |  |
|---|---|
| Route | [`POST /api/admin/invite-links`](api.md#post-apiadmininvite-links) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `days` | integer | yes | 1 to 365 |  |
| `label` | string | yes | 1 to 80 characters |  |
| `max_uses` | integer | yes | 1 to 1000 |  |
| `role` | string | no | one of `user`, `viewer`; default `user` | The role each person who joins gets: user, or viewer (reads only). |

## admin_create_user

Make a new account and its first login link, to hand to the person. role is admin, user or viewer (reads only). account_expires_at, when given, is when the account stops working. Answers with user_id and the link. Answers with login_url (open it to sign in), expires_at and max_uses. The link works once and expires within a day (links made with an API key are held to that; a browser can make longer or reusable ones). Any older link the account could still use stops working; its signed-in devices stay signed in. Revoking or deleting this API key voids the link while it is unused, and signs out every device it signed in.

|  |  |
|---|---|
| Route | [`POST /api/admin/users`](api.md#post-apiadminusers) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `account_expires_at` | string (date-time) or null | no |  | When the account stops working (RFC 3339). Left out: never. expires_in_minutes is the login link's expiry, not this. |
| `display_name` | string | yes | 1 to 80 characters |  |
| `expires_in_minutes` | integer or null | no | 0 to 525600 | 0 never expires. Default auth.login_token_ttl_seconds for a link that works once, auth.multi_use_login_token_ttl_seconds otherwise. |
| `max_uses` | integer or null | no | 0 to 1000 | Sign-ins the link allows: 1-1000, or 0 for unlimited. Default 1. |
| `role` | string | yes | one of `admin`, `user`, `viewer` |  |

## admin_delete_invite_link

Take an invite link off the list and stop it working. The accounts it made stay. admin_restore_invite_link undoes it for a few minutes.

|  |  |
|---|---|
| Route | [`POST /api/admin/invite-links/{link_id}/delete`](api.md#post-apiadmininvite-linkslink_iddelete) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `link_id` | string | yes |  | The link's id, from GET /api/admin/invite-links (admin_list_invite_links over MCP). |

## admin_delete_invite_link_bulk

Runs admin_delete_invite_link once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/admin/invite-links/delete`](api.md#post-apibulkadmininvite-linksdelete) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].link_id` | string | yes |  | The link's id, from GET /api/admin/invite-links (admin_list_invite_links over MCP). |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |

## admin_delete_user

Remove an account for good, with its sessions, login link and API keys. Cannot be undone: admin_set_user_disabled is the reversible version. Only the owner deletes an admin; nobody deletes the owner or themselves.

|  |  |
|---|---|
| Route | [`POST /api/admin/users/{user_id}/delete`](api.md#post-apiadminusersuser_iddelete) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |

## admin_delete_user_bulk

Runs admin_delete_user once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/admin/users/delete`](api.md#post-apibulkadminusersdelete) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |

## admin_get_theme_defaults

The theme list everyone without their own list sees. themes is null while the built-in ones apply.

|  |  |
|---|---|
| Route | [`GET /api/admin/theme-defaults`](api.md#get-apiadmintheme-defaults) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|

## admin_list_invite_links

Group invite links, a page at a time: label, places used and left, expiry, and whether each still works. The links themselves are never shown again after creation. next is the offset of the following page, or null on the last one.

|  |  |
|---|---|
| Route | [`GET /api/admin/invite-links`](api.md#get-apiadmininvite-links) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `dir` | string | no | one of `asc`, `desc` | Default asc. |
| `limit` | integer | no | 1 to 1000; default `200` | Rows to return. Default 200. |
| `offset` | integer | no | at least 0 | Rows to skip: the next value of the previous page. |
| `q` | string | no |  | Keep links whose label or maker contains this, in any case. |
| `sort` | string | no | one of `label`, `used`, `expires_at` | Field to sort the whole list by. Rows without it go last. |

## admin_list_user_sessions

Where an account is signed in: every session, with when it started and was last seen. Addresses are shown to the owner only, and only the owner sees the owner's.

|  |  |
|---|---|
| Route | [`GET /api/admin/users/{user_id}/sessions`](api.md#get-apiadminusersuser_idsessions) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `limit` | integer | no | 1 to 1000; default `200` | Rows to return. Default 200. |
| `offset` | integer | no | at least 0 | Rows to skip: the next value of the previous page. |
| `user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |

## admin_list_users

Accounts, a page at a time, including disabled ones, with each one's role and which is the owner. next is the offset of the following page, or null on the last one.

|  |  |
|---|---|
| Route | [`GET /api/admin/users`](api.md#get-apiadminusers) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `dir` | string | no | one of `asc`, `desc` | Default asc. |
| `limit` | integer | no | 1 to 1000; default `200` | Rows to return. Default 200. |
| `offset` | integer | no | at least 0 | Rows to skip: the next value of the previous page. |
| `q` | string | no |  | Keep accounts whose name or username contains this, in any case. |
| `sort` | string | no | one of `display_name`, `role`, `disabled`, `created_at` | Field to sort the whole list by. Rows without it go last. |

## admin_reissue_login

For someone who lost their device or their link: a fresh login link for their account. Answers with login_url (open it to sign in), expires_at and max_uses. The link works once and expires within a day (links made with an API key are held to that; a browser can make longer or reusable ones). Any older link the account could still use stops working; its signed-in devices stay signed in. Revoking or deleting this API key voids the link while it is unused, and signs out every device it signed in.

|  |  |
|---|---|
| Route | [`POST /api/admin/users/{user_id}/reissue-login`](api.md#post-apiadminusersuser_idreissue-login) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `expires_in_minutes` | integer or null | no | 0 to 525600 | 0 never expires. Default auth.login_token_ttl_seconds for a link that works once, auth.multi_use_login_token_ttl_seconds otherwise. |
| `max_uses` | integer or null | no | 0 to 1000 | Sign-ins the link allows: 1-1000, or 0 for unlimited. Default 1. |
| `user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |

## admin_rename_invite_link

Change the label people see on an invite link's join page (1-80 characters). expect, when given, is the label you think it has now.

|  |  |
|---|---|
| Route | [`POST /api/admin/invite-links/{link_id}/rename`](api.md#post-apiadmininvite-linkslink_idrename) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `expect` | string or null | no |  | The label you think it has. Answers 409 if it has another. |
| `label` | string | yes | 1 to 80 characters | 1-80 characters. |
| `link_id` | string | yes |  | The link's id, from GET /api/admin/invite-links (admin_list_invite_links over MCP). |

## admin_rename_user

Change another account's display name (1-80 characters). Only the owner renames an admin. expect, when given, is the name you think it has now; if it changed meanwhile the rename is refused with the current name.

|  |  |
|---|---|
| Route | [`POST /api/admin/users/{user_id}/rename`](api.md#post-apiadminusersuser_idrename) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `display_name` | string | yes | 1 to 80 characters | 1-80 characters. |
| `expect` | string or null | no |  | The name you think they have. Answers 409 if it is another. |
| `user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |

## admin_reset_two_factor

For someone who lost both their phone and their recovery codes: switches their two-factor sign-in off so a login link lets them in again. Only the owner resets an admin's; the owner's is reset from a shell.

|  |  |
|---|---|
| Route | [`POST /api/admin/users/{user_id}/reset-two-factor`](api.md#post-apiadminusersuser_idreset-two-factor) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |

## admin_reset_two_factor_bulk

Runs admin_reset_two_factor once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/admin/users/reset-two-factor`](api.md#post-apibulkadminusersreset-two-factor) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |

## admin_restore_invite_link

Bring back an invite link deleted in the last few minutes, working as before. The link then counts as this key's: revoking the key switches it off.

|  |  |
|---|---|
| Route | [`POST /api/admin/invite-links/{link_id}/restore`](api.md#post-apiadmininvite-linkslink_idrestore) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `link_id` | string | yes |  | The link's id, from GET /api/admin/invite-links (admin_list_invite_links over MCP). |

## admin_restore_invite_link_bulk

Runs admin_restore_invite_link once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/admin/invite-links/restore`](api.md#post-apibulkadmininvite-linksrestore) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].link_id` | string | yes |  | The link's id, from GET /api/admin/invite-links (admin_list_invite_links over MCP). |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |

## admin_revoke_access

For an account that may be compromised: ends every session and voids its live login link and every API key it holds, at once. The account stays enabled; admin_reissue_login lets its owner back in. The owner and your own account cannot be revoked.

|  |  |
|---|---|
| Route | [`POST /api/admin/users/{user_id}/revoke-access`](api.md#post-apiadminusersuser_idrevoke-access) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |

## admin_revoke_access_bulk

Runs admin_revoke_access once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/admin/users/revoke-access`](api.md#post-apibulkadminusersrevoke-access) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |

## admin_revoke_invite_link

Stop an invite link from letting anyone else join or sign in through it. Accounts it already made keep working. Cannot be switched back on.

|  |  |
|---|---|
| Route | [`POST /api/admin/invite-links/{link_id}/revoke`](api.md#post-apiadmininvite-linkslink_idrevoke) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `link_id` | string | yes |  | The link's id, from GET /api/admin/invite-links (admin_list_invite_links over MCP). |

## admin_revoke_invite_link_bulk

Runs admin_revoke_invite_link once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/admin/invite-links/revoke`](api.md#post-apibulkadmininvite-linksrevoke) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].link_id` | string | yes |  | The link's id, from GET /api/admin/invite-links (admin_list_invite_links over MCP). |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |

## admin_revoke_user_session

End one of an account's sessions, rather than all of them with admin_revoke_access.

|  |  |
|---|---|
| Route | [`POST /api/admin/users/{user_id}/sessions/{session_id}/revoke`](api.md#post-apiadminusersuser_idsessionssession_idrevoke) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `session_id` | string | yes |  | The device's id, from GET /api/account/sessions or GET /api/admin/users/{user_id}/sessions (list_my_sessions or admin_list_user_sessions over MCP). |
| `user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |

## admin_revoke_user_session_bulk

Runs admin_revoke_user_session once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/admin/users/sessions/revoke`](api.md#post-apibulkadminuserssessionsrevoke) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].session_id` | string | yes |  | The device's id, from GET /api/account/sessions or GET /api/admin/users/{user_id}/sessions (list_my_sessions or admin_list_user_sessions over MCP). |
| `items[].user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |

## admin_set_invite_link_limits

Set how many people the link may take in (never fewer than have joined) and, when days is given, a new expiry counted from now. The link then counts as this key's: revoking the key switches it off.

|  |  |
|---|---|
| Route | [`POST /api/admin/invite-links/{link_id}/limits`](api.md#post-apiadmininvite-linkslink_idlimits) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `days` | integer or null | no | 1 to 365 | Counted from now. Leave out to keep the expiry. |
| `link_id` | string | yes |  | The link's id, from GET /api/admin/invite-links (admin_list_invite_links over MCP). |
| `max_uses` | integer | yes | 1 to 1000 | Not fewer than have joined. |

## admin_set_theme_defaults

Replace the theme list everyone without their own list sees, 1 to 40 themes in the Theme schema of the API reference. null puts the built-in themes back.

|  |  |
|---|---|
| Route | [`POST /api/admin/theme-defaults`](api.md#post-apiadmintheme-defaults) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `builtins` | integer | no |  | Which built-in themes this list has seen: the highest since in Theme.builtIn (static/js/theme.js) when it was saved. Built-in themes added after that join the list the browser shows. Left out: 0, the first ones. |
| `themes` | array of object or null | no |  | 1 to 40 themes. null goes back to the built-in ones. |
| `themes[].accent` | string | yes |  | The main color: what you can press. |
| `themes[].background` | string | no |  | The page. Left out: the mode's own. |
| `themes[].button` | object or null | no |  | How the theme's buttons look. A choice left out is the default (rounded, normal, raised, normal). |
| `themes[].button.case` | string | no | one of `normal`, `upper` |  |
| `themes[].button.depth` | string | no | one of `flat`, `raised`, `glossy` |  |
| `themes[].button.shape` | string | no | one of `square`, `soft`, `rounded`, `pill` |  |
| `themes[].button.weight` | string | no | one of `normal`, `medium`, `bold` |  |
| `themes[].dark` | object or null | no |  | A light theme's colors for dark mode, kept while it is light. Switching the theme to dark swaps them in. A light theme's light (or a dark theme's dark) is dropped. |
| `themes[].dark.accent` | string | yes |  | The main color: what you can press. |
| `themes[].dark.background` | string | no |  | The page. Left out: the mode's own. |
| `themes[].dark.overrides` | map of string | no |  | Worked-out colors replaced by name: text, accent, accentFg, accentText, second, secondFg, secondText, link, navLink, background, surface, nested, chrome, bar (the bar across the top), barText, info, infoBorder, border, rowOdd and rowEven (alternating table rows), and for each button variant V (Secondary, Success, Danger, Warning, Info, Light, Dark) btnV, btnVFg and btnVText. Leaving one out puts the readable color back. |
| `themes[].dark.second` | string | yes |  | Says where you are: active nav item, headings, info. |
| `themes[].dark.surface` | string | no |  | Cards. Left out: the mode's own. |
| `themes[].id` | string | yes |  | Lower-case letters, digits, - and _, up to 32. |
| `themes[].light` | object or null | no |  | A dark theme's colors for light mode, kept while it is dark. Switching the theme to light swaps them in. |
| `themes[].light.accent` | string | yes |  | The main color: what you can press. |
| `themes[].light.background` | string | no |  | The page. Left out: the mode's own. |
| `themes[].light.overrides` | map of string | no |  | Worked-out colors replaced by name: text, accent, accentFg, accentText, second, secondFg, secondText, link, navLink, background, surface, nested, chrome, bar (the bar across the top), barText, info, infoBorder, border, rowOdd and rowEven (alternating table rows), and for each button variant V (Secondary, Success, Danger, Warning, Info, Light, Dark) btnV, btnVFg and btnVText. Leaving one out puts the readable color back. |
| `themes[].light.second` | string | yes |  | Says where you are: active nav item, headings, info. |
| `themes[].light.surface` | string | no |  | Cards. Left out: the mode's own. |
| `themes[].mode` | string | yes | one of `light`, `dark` |  |
| `themes[].name` | string | yes |  | 1 to 60 characters. |
| `themes[].overrides` | map of string | no |  | Worked-out colors replaced by name: text, accent, accentFg, accentText, second, secondFg, secondText, link, navLink, background, surface, nested, chrome, bar (the bar across the top), barText, info, infoBorder, border, rowOdd and rowEven (alternating table rows), and for each button variant V (Secondary, Success, Danger, Warning, Info, Light, Dark) btnV, btnVFg and btnVText. Leaving one out puts the readable color back. |
| `themes[].second` | string | yes |  | Says where you are: active nav item, headings, info. |
| `themes[].surface` | string | no |  | Cards. Left out: the mode's own. |

## admin_set_user_disabled

Switch an account off (disabled: true) or back on (false). Disabling signs it out everywhere and voids its live login link; its API keys stop working while it is off. Reversible. The owner and your own account cannot be disabled.

|  |  |
|---|---|
| Route | [`POST /api/admin/users/{user_id}/disabled`](api.md#post-apiadminusersuser_iddisabled) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `disabled` | boolean | yes |  |  |
| `user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |

## admin_set_user_disabled_bulk

Runs admin_set_user_disabled once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/admin/users/disabled`](api.md#post-apibulkadminusersdisabled) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].disabled` | boolean | no |  |  |
| `items[].user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |
| `shared.disabled` | boolean | no |  |  |

## admin_set_user_expiry

expires_at is when the account stops working (RFC 3339), or null for never. Once it passes the account counts as disabled: sign-in, its sessions and its keys stop, and housekeeping disables it and revokes its access. A later expiry does not re-enable an account housekeeping already disabled. It must be in the future. The owner's account never expires; only the owner sets an admin's.

|  |  |
|---|---|
| Route | [`POST /api/admin/users/{user_id}/expiry`](api.md#post-apiadminusersuser_idexpiry) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `expires_at` | string (date-time) or null | yes |  | When the account stops working (RFC 3339), or null for never. |
| `user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |

## admin_set_user_role

Make an account an admin, an ordinary user, or a viewer, who may read but change nothing. Only the owner takes an admin's rights away; the owner is always an admin, and nobody changes their own role. Becoming an admin ends the account's sessions and live login link.

|  |  |
|---|---|
| Route | [`POST /api/admin/users/{user_id}/role`](api.md#post-apiadminusersuser_idrole) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `role` | string | yes | one of `admin`, `user`, `viewer` |  |
| `user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |

## admin_set_user_role_bulk

Runs admin_set_user_role once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/admin/users/role`](api.md#post-apibulkadminusersrole) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].role` | string | no | one of `admin`, `user`, `viewer` |  |
| `items[].user_id` | integer | yes | at least 1 | The account's id, from GET /api/admin/users (admin_list_users over MCP). |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |
| `shared.role` | string | no | one of `admin`, `user`, `viewer` |  |

## admin_switch_on_invite_link

Undo admin_revoke_invite_link: anyone still holding the link can use it again. The link then counts as this key's: revoking the key switches it off.

|  |  |
|---|---|
| Route | [`POST /api/admin/invite-links/{link_id}/switch-on`](api.md#post-apiadmininvite-linkslink_idswitch-on) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `link_id` | string | yes |  | The link's id, from GET /api/admin/invite-links (admin_list_invite_links over MCP). |

## admin_switch_on_invite_link_bulk

Runs admin_switch_on_invite_link once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/admin/invite-links/switch-on`](api.md#post-apibulkadmininvite-linksswitch-on) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].link_id` | string | yes |  | The link's id, from GET /api/admin/invite-links (admin_list_invite_links over MCP). |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |

## cancel_my_login_link

Void your account's live login link without making a new one. Devices it already signed in stay signed in. Answers with removed: 0 or 1.

|  |  |
|---|---|
| Route | [`POST /api/account/login-link/cancel`](api.md#post-apiaccountlogin-linkcancel) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|

## create_my_login_link

A link that signs your own account in on a browser or another device. An API key may ask only if your account let it, from a browser session (POST /api/keys/{key_id}/sign-in); its link works once, for at most 15 minutes. Only works if this key was allowed to make sign-in links, on the API keys card. Answers with login_url (open it to sign in; it works once, for at most 15 minutes), expires_at and max_uses. Any older link the account could still use stops working; its signed-in devices stay signed in. Revoking or deleting this API key voids the link while it is unused, and signs out every device it signed in.

|  |  |
|---|---|
| Route | [`POST /api/account/login-link`](api.md#post-apiaccountlogin-link) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `expires_in_minutes` | integer or null | no | 0 to 525600 | 0 never expires. Default auth.login_token_ttl_seconds for a link that works once, auth.multi_use_login_token_ttl_seconds otherwise. |
| `max_uses` | integer or null | no | 0 to 1000 | Sign-ins the link allows: 1-1000, or 0 for unlimited. Default 1. |

## label_my_session

Give one of your devices a name (at most 80 characters; empty clears it). expect, when given, is the name you think it has now.

|  |  |
|---|---|
| Route | [`POST /api/account/sessions/{session_id}/label`](api.md#post-apiaccountsessionssession_idlabel) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `expect` | string or null | no |  | The name you think it has. Answers 409 if it has another. |
| `label` | string | yes | at most 80 characters | At most 80 characters. |
| `session_id` | string | yes |  | The device's id, from GET /api/account/sessions or GET /api/admin/users/{user_id}/sessions (list_my_sessions or admin_list_user_sessions over MCP). |

## list_my_sessions

Where your account is signed in, a page at a time: id, when it started and was last seen, the browser, and the name you gave it. Through an API key no device is current. next is the offset of the following page, or null on the last one.

|  |  |
|---|---|
| Route | [`GET /api/account/sessions`](api.md#get-apiaccountsessions) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `limit` | integer | no | 1 to 1000; default `200` | Rows to return. Default 200. |
| `offset` | integer | no | at least 0 | Rows to skip: the next value of the previous page. |

## list_team

People with an active account, a page at a time: id and display name. Use the id wherever another tool asks for a user. next is the offset of the following page, or null on the last one.

|  |  |
|---|---|
| Route | [`GET /api/team`](api.md#get-apiteam) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `limit` | integer | no | 1 to 1000; default `200` | Rows to return. Default 200. |
| `offset` | integer | no | at least 0 | Rows to skip: the next value of the previous page. |

## rename_account

Change your own display name (1-80 characters). expect, when given, is the name you think it has now; if someone changed it meanwhile the rename is refused with the current name, so nothing is overwritten unseen.

|  |  |
|---|---|
| Route | [`POST /api/account/rename`](api.md#post-apiaccountrename) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `display_name` | string | yes | 1 to 80 characters |  |
| `expect` | string or null | no |  |  |

## revoke_my_other_sessions

End every session your account has: through an API key there is no current device to keep, so every browser signs in again. API keys keep working. Answers with how many were removed.

|  |  |
|---|---|
| Route | [`POST /api/account/sessions/revoke-others`](api.md#post-apiaccountsessionsrevoke-others) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|

## revoke_my_session

End one of your signed-in sessions; that browser has to sign in again.

|  |  |
|---|---|
| Route | [`POST /api/account/sessions/{session_id}/revoke`](api.md#post-apiaccountsessionssession_idrevoke) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `session_id` | string | yes |  | The device's id, from GET /api/account/sessions or GET /api/admin/users/{user_id}/sessions (list_my_sessions or admin_list_user_sessions over MCP). |

## revoke_my_session_bulk

Runs revoke_my_session once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/account/sessions/revoke`](api.md#post-apibulkaccountsessionsrevoke) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].session_id` | string | yes |  | The device's id, from GET /api/account/sessions or GET /api/admin/users/{user_id}/sessions (list_my_sessions or admin_list_user_sessions over MCP). |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |

## set_shortcuts

Replace your rebound keyboard shortcuts: action id to its list of keys, such as "undo": ["Mod+Z"] (Mod is Cmd on a Mac, Ctrl elsewhere). Send the whole map; an empty list switches an action's keys off, and {} puts every key back to its default. whoami shows the current map.

|  |  |
|---|---|
| Route | [`POST /api/account/shortcuts`](api.md#post-apiaccountshortcuts) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `shortcuts` | map of array of string | yes |  | Action id to the keys bound to it. Replaces the whole map; {} puts every key back to its default. Action ids the screens do not know are ignored. |

## set_theme

Switch to another theme from your list (or the defaults), by its id.

|  |  |
|---|---|
| Route | [`POST /api/account/theme`](api.md#post-apiaccounttheme) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `theme_id` | string | yes |  | A theme's id. Empty for the first in the list. |

## set_themes

Replace your whole list of color themes (1 to 40) and pick the one you use. themes: null goes back to following the app's defaults. A theme is the Theme schema in the API reference (config/api.json): id, name, mode light|dark, accent, second, and optional colors as #rrggbb. whoami shows the current list.

|  |  |
|---|---|
| Route | [`POST /api/account/themes`](api.md#post-apiaccountthemes) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `builtins` | integer | no |  | Which built-in themes this list has seen: the highest since in Theme.builtIn (static/js/theme.js) when it was saved. Built-in themes added after that join the list the browser shows. Left out: 0, the first ones. |
| `theme_id` | string | no |  | The theme you use. |
| `themes` | array of object or null | no |  | Your whole list, 1 to 40 themes. null goes back to following the app's defaults. |
| `themes[].accent` | string | yes |  | The main color: what you can press. |
| `themes[].background` | string | no |  | The page. Left out: the mode's own. |
| `themes[].button` | object or null | no |  | How the theme's buttons look. A choice left out is the default (rounded, normal, raised, normal). |
| `themes[].button.case` | string | no | one of `normal`, `upper` |  |
| `themes[].button.depth` | string | no | one of `flat`, `raised`, `glossy` |  |
| `themes[].button.shape` | string | no | one of `square`, `soft`, `rounded`, `pill` |  |
| `themes[].button.weight` | string | no | one of `normal`, `medium`, `bold` |  |
| `themes[].dark` | object or null | no |  | A light theme's colors for dark mode, kept while it is light. Switching the theme to dark swaps them in. A light theme's light (or a dark theme's dark) is dropped. |
| `themes[].dark.accent` | string | yes |  | The main color: what you can press. |
| `themes[].dark.background` | string | no |  | The page. Left out: the mode's own. |
| `themes[].dark.overrides` | map of string | no |  | Worked-out colors replaced by name: text, accent, accentFg, accentText, second, secondFg, secondText, link, navLink, background, surface, nested, chrome, bar (the bar across the top), barText, info, infoBorder, border, rowOdd and rowEven (alternating table rows), and for each button variant V (Secondary, Success, Danger, Warning, Info, Light, Dark) btnV, btnVFg and btnVText. Leaving one out puts the readable color back. |
| `themes[].dark.second` | string | yes |  | Says where you are: active nav item, headings, info. |
| `themes[].dark.surface` | string | no |  | Cards. Left out: the mode's own. |
| `themes[].id` | string | yes |  | Lower-case letters, digits, - and _, up to 32. |
| `themes[].light` | object or null | no |  | A dark theme's colors for light mode, kept while it is dark. Switching the theme to light swaps them in. |
| `themes[].light.accent` | string | yes |  | The main color: what you can press. |
| `themes[].light.background` | string | no |  | The page. Left out: the mode's own. |
| `themes[].light.overrides` | map of string | no |  | Worked-out colors replaced by name: text, accent, accentFg, accentText, second, secondFg, secondText, link, navLink, background, surface, nested, chrome, bar (the bar across the top), barText, info, infoBorder, border, rowOdd and rowEven (alternating table rows), and for each button variant V (Secondary, Success, Danger, Warning, Info, Light, Dark) btnV, btnVFg and btnVText. Leaving one out puts the readable color back. |
| `themes[].light.second` | string | yes |  | Says where you are: active nav item, headings, info. |
| `themes[].light.surface` | string | no |  | Cards. Left out: the mode's own. |
| `themes[].mode` | string | yes | one of `light`, `dark` |  |
| `themes[].name` | string | yes |  | 1 to 60 characters. |
| `themes[].overrides` | map of string | no |  | Worked-out colors replaced by name: text, accent, accentFg, accentText, second, secondFg, secondText, link, navLink, background, surface, nested, chrome, bar (the bar across the top), barText, info, infoBorder, border, rowOdd and rowEven (alternating table rows), and for each button variant V (Secondary, Success, Danger, Warning, Info, Light, Dark) btnV, btnVFg and btnVText. Leaving one out puts the readable color back. |
| `themes[].second` | string | yes |  | Says where you are: active nav item, headings, info. |
| `themes[].surface` | string | no |  | Cards. Left out: the mode's own. |

## whoami

The account this API key belongs to, the role it acts with (role -- never higher than the key's own scope), and the account's own role.

|  |  |
|---|---|
| Route | [`GET /api/me`](api.md#get-apime) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|

## list_batches

Batches in the team's order, a page at a time, with progress (images, included, completed, ais, auto, stored, assignees, live activity) and the folders. Archived ones only with archived: true. next is the offset of the following page, or null.

|  |  |
|---|---|
| Route | [`GET /api/ais/batches`](api.md#get-apiaisbatches) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `archived` | boolean | no |  |  |
| `folder_id` | integer | no | at least 1 | The folder's id, from list_folders. |
| `limit` | integer | no | 1 to 1000 | Rows to return. Default 200. |
| `offset` | integer | no | at least 0 | Rows to skip: the next value of the previous page. |
| `q` | string | no |  | Only names containing this. |

## list_folders

The batch folders, each with its parent and order.

|  |  |
|---|---|
| Route | [`GET /api/ais/folders`](api.md#get-apiaisfolders) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|

## get_batch

One batch whole: its images (key, cell, dir, files per role with sha and whether the server has them stored), adds, done marks (skipped), excluded images, assignment. Admins also see original names.

|  |  |
|---|---|
| Route | [`GET /api/ais/batches/{batch_id}`](api.md#get-apiaisbatchesbatch_id) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |

## batch_status

Per image, a page at a time: files and how many are stored, accepted AIS (and how many by auto mode), done, duplicate of, assignee, included.

|  |  |
|---|---|
| Route | [`GET /api/ais/batches/{batch_id}/status`](api.md#get-apiaisbatchesbatch_idstatus) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `limit` | integer | no | 1 to 1000 | Rows to return. Default 200. |
| `offset` | integer | no | at least 0 | Rows to skip: the next value of the previous page. |

## batch_channels

The channels of the batch's included .czi files, by name, with how many files have each.

|  |  |
|---|---|
| Route | [`GET /api/ais/batches/{batch_id}/channels`](api.md#get-apiaisbatchesbatch_idchannels) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |

## list_results

Accepted AIS, a page at a time: one batch's, or every batch's without batch_id; image narrows it to one image. Each row's numbers as the export has them (length_um, ...), its rev for update_result, created_by. pixels only with include_pixels: true.

|  |  |
|---|---|
| Route | [`GET /api/ais/results`](api.md#get-apiaisresults) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | no | at least 1 | The batch's id, from list_batches. |
| `image` | string | no |  | The image's key in the batch (batch_status or get_batch: key). |
| `include_pixels` | boolean | no |  |  |
| `limit` | integer | no | 1 to 1000 | Rows to return. Default 200. |
| `offset` | integer | no | at least 0 | Rows to skip: the next value of the previous page. |

## list_measurements

Lines recorded with the Measure tool, a page at a time: one batch's, or every batch's; image narrows it.

|  |  |
|---|---|
| Route | [`GET /api/ais/measurements`](api.md#get-apiaismeasurements) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | no | at least 1 | The batch's id, from list_batches. |
| `image` | string | no |  | The image's key in the batch (batch_status or get_batch: key). |
| `limit` | integer | no | 1 to 1000 | Rows to return. Default 200. |
| `offset` | integer | no | at least 0 | Rows to skip: the next value of the previous page. |

## list_measure_types

The team's types a recorded line can have.

|  |  |
|---|---|
| Route | [`GET /api/ais/measure-types`](api.md#get-apiaismeasure-types) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|

## create_batch

A new batch with no images yet, in that folder or at the top. Add files with add_files_to_batch.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches`](api.md#post-apiaisbatches) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `folder_id` | integer | no | at least 1 | The folder's id, from list_folders. |
| `name` | string | yes |  |  |

## create_batch_from_files

A new batch from files you hashed (name, rel, sha, size each), grouped into images as the browser does (<cell>.tif raw, '<cell>.tif - Processed method 2.5.tif' processed, .czi, *_zNNN.tif with stack). Duplicates start left out. Answers with the files the server still needs and how to upload them (POST each file's bytes to /api/ais/files with your API key).

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/upload`](api.md#post-apiaisbatchesupload) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `channels` | array of object | no |  | Channel roles per layout: [{layout: {kind, names}, roles: [{role: ais \| soma \| other, label}]}], one role per channel, exactly one ais, at most one soma, a label for each other. Images whose file layout matches get them; left out, the AIS is guessed (a .czi's Alexa Fluor 488, a TIFF's first plane). |
| `channels[].layout` | object | no |  |  |
| `channels[].roles` | array of any | no |  |  |
| `czi_stack` | object | no |  | Z-stack .czi files (files with zstack) become one image each: {apotome: sectioned (default) \| widefield}, how an ApoTome stack's grid phases are made into slices. Their AIS channel is guessed (Alexa Fluor 488) unless channels says. |
| `czi_stack.apotome` | string | no | one of `sectioned`, `widefield` |  |
| `files` | array of object | yes |  | The files, hashed on your side: name and rel (path inside the picked folder) as they are, sha256 of the bytes, size in bytes. |
| `files[].layout` | object | no |  | Its channels, for channels: {kind: czi \| tiff, names: [...]} (a .czi's channel names; a TIFF's planes as Red/Green/Blue or Channel N). |
| `files[].modified` | number | no |  |  |
| `files[].name` | string | yes |  |  |
| `files[].rel` | string | yes |  |  |
| `files[].sha` | string | yes |  | sha-256 of the file, lower-case hex. |
| `files[].size` | integer | yes |  |  |
| `files[].zstack` | object | no |  | A .czi with more than one Z plane (a Z-stack): {slices, phases (ApoTome grid phases, 1 without), z_step_um, pixel_um} from its metadata (Scaling X and Z, in microns). Needs layout. |
| `name` | string | yes |  |  |
| `randomize` | boolean | no |  | Blind the names (default true): images get random n-n-n names, the originals kept for admins. |
| `stack` | object | no |  | Z-stack TIFF slices (name_zNNN.tif) become one image each stack: {plane: 0 red \| 1 green \| 2 blue \| 3, z_step_um, pixel_um}. |
| `stack.pixel_um` | number | no |  |  |
| `stack.plane` | integer | no |  |  |
| `stack.z_step_um` | number | no |  |  |
| `translations` | array of object | no |  | __Translation.txt files that came with them: [{dir, text}]. |
| `translations[].dir` | string | no |  |  |
| `translations[].text` | string | no |  |  |

## add_files_to_batch

More files into an existing batch, as create_batch_from_files. add_name names this add (a folder name).

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/upload`](api.md#post-apiaisbatchesbatch_idupload) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `add_name` | string | no |  |  |
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `channels` | array of object | no |  | Channel roles per layout: [{layout: {kind, names}, roles: [{role: ais \| soma \| other, label}]}], one role per channel, exactly one ais, at most one soma, a label for each other. Images whose file layout matches get them; left out, the AIS is guessed (a .czi's Alexa Fluor 488, a TIFF's first plane). |
| `channels[].layout` | object | no |  |  |
| `channels[].roles` | array of any | no |  |  |
| `czi_stack` | object | no |  | Z-stack .czi files (files with zstack) become one image each: {apotome: sectioned (default) \| widefield}, how an ApoTome stack's grid phases are made into slices. Their AIS channel is guessed (Alexa Fluor 488) unless channels says. |
| `czi_stack.apotome` | string | no | one of `sectioned`, `widefield` |  |
| `files` | array of object | yes |  | The files, hashed on your side: name and rel (path inside the picked folder) as they are, sha256 of the bytes, size in bytes. |
| `files[].layout` | object | no |  | Its channels, for channels: {kind: czi \| tiff, names: [...]} (a .czi's channel names; a TIFF's planes as Red/Green/Blue or Channel N). |
| `files[].modified` | number | no |  |  |
| `files[].name` | string | yes |  |  |
| `files[].rel` | string | yes |  |  |
| `files[].sha` | string | yes |  | sha-256 of the file, lower-case hex. |
| `files[].size` | integer | yes |  |  |
| `files[].zstack` | object | no |  | A .czi with more than one Z plane (a Z-stack): {slices, phases (ApoTome grid phases, 1 without), z_step_um, pixel_um} from its metadata (Scaling X and Z, in microns). Needs layout. |
| `randomize` | boolean | no |  | Blind the names (default true): images get random n-n-n names, the originals kept for admins. |
| `stack` | object | no |  | Z-stack TIFF slices (name_zNNN.tif) become one image each stack: {plane: 0 red \| 1 green \| 2 blue \| 3, z_step_um, pixel_um}. |
| `stack.pixel_um` | number | no |  |  |
| `stack.plane` | integer | no |  |  |
| `stack.z_step_um` | number | no |  |  |
| `translations` | array of object | no |  | __Translation.txt files that came with them: [{dir, text}]. |
| `translations[].dir` | string | no |  |  |
| `translations[].text` | string | no |  |  |

## get_channel_layouts

The channel layouts of a batch's images (or one add's): each with its channel names, how many images, the roles in use and how many already have results.

|  |  |
|---|---|
| Route | [`GET /api/ais/batches/{batch_id}/layouts`](api.md#get-apiaisbatchesbatch_idlayouts) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `add` | integer | no |  |  |
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |

## set_channel_roles

Which channel is the AIS, soma/dendrite or other, for a batch's (or one add's) images with those layouts; stack: {z_step_um, pixel_um} also sets its Z-stacks' slice spacing and pixel size (the files don't record them); pixel_um sets the microns per pixel its other images are measured with (null: back to the 40x default). Images now traced from other channels or calibration are no longer done; their results stay (3D measures as measured), so look at them again.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/layouts`](api.md#post-apiaisbatchesbatch_idlayouts) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `add` | integer | no |  |  |
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `channels` | array of object | yes |  | Channel roles per layout: [{layout: {kind, names}, roles: [{role: ais \| soma \| other, label}]}], one role per channel, exactly one ais, at most one soma, a label for each other. Images whose file layout matches get them; left out, the AIS is guessed (a .czi's Alexa Fluor 488, a TIFF's first plane). |
| `channels[].layout` | object | no |  |  |
| `channels[].roles` | array of any | no |  |  |
| `pixel_um` | number or null | no |  |  |
| `stack` | object | no |  |  |
| `stack.pixel_um` | number | no |  |  |
| `stack.z_step_um` | number | no |  |  |

## fill_missing_areas

For a batch's accepted AIS saved before area (and on Z-stacks volume) was measured: trace each again from its saved clicks and settings and, when it comes out on the same pixels, fill in area_blob_um2, area_width_um2 (and volume_voxel_um3, volume_tube_um3); nothing else changes. with_soma: only AIS whose soma distance has been measured. A few at a time: call again with after until remaining is 0.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/fill-areas`](api.md#post-apiaisbatchesbatch_idfill-areas) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `after` | integer | no |  |  |
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `limit` | integer | no |  |  |
| `with_soma` | boolean | no |  |  |

## rename_batch

Its accepted AIS carry the new name too. Whoever opened it, or an admin.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/rename`](api.md#post-apiaisbatchesbatch_idrename) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `name` | string | yes |  |  |

## archive_batch

archived: true hides it from the list (its results stay); false brings it back.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/archive`](api.md#post-apiaisbatchesbatch_idarchive) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `archived` | boolean | yes |  |  |
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |

## set_images_included

Include these images (included: true) or leave them out for the whole team. Left-out images are skipped by auto runs and the report.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/include`](api.md#post-apiaisbatchesbatch_idinclude) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `included` | boolean | yes |  |  |
| `keys` | array of string | yes |  |  |

## set_image_done

Mark (done: true) or unmark an image done by hand: for images with no AIS worth accepting.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/done`](api.md#post-apiaisbatchesbatch_iddone) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `done` | boolean | yes |  |  |
| `image` | string | yes |  | The image's key in the batch (batch_status or get_batch: key). |

## assign_batch

Split the batch's images among people: shares [{user_id, percent}] (ids from list_team). An empty list clears it.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/assign`](api.md#post-apiaisbatchesbatch_idassign) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `shares` | array of object | yes |  |  |

## order_batches

The team's priority order: batch ids, first on top.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/order`](api.md#post-apiaisbatchesorder) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `ids` | array of integer | yes |  |  |

## move_batches

Those batches into that folder; folder_id null for the top.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/move`](api.md#post-apiaisbatchesmove) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `folder_id` | integer or null | yes |  | The parent folder's id, or null for the top. |
| `ids` | array of integer | yes |  |  |

## create_folder

A new folder, first in its parent (null: the top).

|  |  |
|---|---|
| Route | [`POST /api/ais/folders`](api.md#post-apiaisfolders) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `name` | string | yes |  |  |
| `parent_id` | integer or null | no |  | The parent folder's id, or null for the top. |

## rename_folder



|  |  |
|---|---|
| Route | [`POST /api/ais/folders/{folder_id}/rename`](api.md#post-apiaisfoldersfolder_idrename) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `folder_id` | integer | yes | at least 1 | The folder's id, from list_folders. |
| `name` | string | yes |  |  |

## move_folder

Into another folder; parent_id null for the top.

|  |  |
|---|---|
| Route | [`POST /api/ais/folders/{folder_id}/move`](api.md#post-apiaisfoldersfolder_idmove) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `folder_id` | integer | yes | at least 1 | The folder's id, from list_folders. |
| `parent_id` | integer or null | yes |  | The parent folder's id, or null for the top. |

## order_folders

The order of one folder's folders (parent_id null: the top).

|  |  |
|---|---|
| Route | [`POST /api/ais/folders/order`](api.md#post-apiaisfoldersorder) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `ids` | array of integer | yes |  |  |
| `parent_id` | integer or null | yes |  | The parent folder's id, or null for the top. |

## get_treatments

Each image's original name, saved treatment and the guessed one.

|  |  |
|---|---|
| Route | [`GET /api/ais/batches/{batch_id}/treatments`](api.md#get-apiaisbatchesbatch_idtreatments) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |

## set_treatments

treatments: {image key: treatment name}; "" takes one off.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/treatments`](api.md#post-apiaisbatchesbatch_idtreatments) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `treatments` | object | yes |  |  |

## get_translation

The batch's original/random name per file, as text.

|  |  |
|---|---|
| Route | [`GET /api/ais/batches/{batch_id}/translation.txt`](api.md#get-apiaisbatchesbatch_idtranslationtxt) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |

## load_translation

For a batch blinded somewhere else: the original names of the files it names.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/translation`](api.md#post-apiaisbatchesbatch_idtranslation) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `text` | string | yes |  |  |

## rerandomize_add

New random names for one add of the batch (add_id from get_batch adds, or "earlier"); its results, done marks, exclusions and assignment move with them.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/adds/{add_id}/randomize`](api.md#post-apiaisbatchesbatch_idaddsadd_idrandomize) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `add_id` | string | yes |  |  |
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |

## get_backup

The batch as data, with its results and recorded lines and the people in it: what a restorable backup's manifest holds.

|  |  |
|---|---|
| Route | [`GET /api/ais/batches/{batch_id}/backup`](api.md#get-apiaisbatchesbatch_idbackup) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |

## save_result

Accept an AIS on an image: row as trace_click or detect_image gives it (or your own numbers). Give a client_id so a retry never saves it twice.

|  |  |
|---|---|
| Route | [`POST /api/ais/results`](api.md#post-apiaisresults) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `client_id` | string | no |  | Your own id for this create (8-64 letters, digits, -). Sent again, it finds the first one instead of adding a second. |
| `image` | string | yes |  | The image's key in the batch (batch_status or get_batch: key). |
| `row` | object | yes |  | The row as save_result takes it: the 'row' a trace_click or detect_image candidate gives, or your own numbers (app/models/ais.py RESULT_NUMBERS). |

## update_result

An accepted AIS traced again: it keeps its number and origin. Whoever accepted it, the image's assignee, or an admin.

|  |  |
|---|---|
| Route | [`POST /api/ais/results/{result_id}/update`](api.md#post-apiaisresultsresult_idupdate) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `expect` | integer | no | at least 0 | The rev you last saw (optional). If someone changed it since, the call is refused with the current one. |
| `result_id` | integer | yes | at least 1 | The result's id, from list_results. |
| `row` | object | yes |  | The row as save_result takes it: the 'row' a trace_click or detect_image candidate gives, or your own numbers (app/models/ais.py RESULT_NUMBERS). |

## set_result_soma

soma: {soma_um, soma_px, soma_ais_x, soma_ais_y, soma_x, soma_y}, plus on a Z-stack soma_xy_um and soma_dz_um (soma_um is then the 3D distance), or null to clear it. The trace stays as it is.

|  |  |
|---|---|
| Route | [`POST /api/ais/results/{result_id}/soma`](api.md#post-apiaisresultsresult_idsoma) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `expect` | integer | no | at least 0 | The rev you last saw (optional). If someone changed it since, the call is refused with the current one. |
| `result_id` | integer | yes | at least 1 | The result's id, from list_results. |
| `soma` | object or null | yes |  |  |

## delete_result

One accepted AIS gone; the image's others renumbered. Whoever accepted it, the image's assignee, or an admin. Cannot be undone.

|  |  |
|---|---|
| Route | [`POST /api/ais/results/{result_id}/delete`](api.md#post-apiaisresultsresult_iddelete) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `expect` | integer | no | at least 0 | The rev you last saw (optional). If someone changed it since, the call is refused with the current one. |
| `result_id` | integer | yes | at least 1 | The result's id, from list_results. |

## add_measurement

A line measured on an image (the Measure tool's Record).

|  |  |
|---|---|
| Route | [`POST /api/ais/measurements`](api.md#post-apiaismeasurements) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `client_id` | string | no |  | Your own id for this create (8-64 letters, digits, -). Sent again, it finds the first one instead of adding a second. |
| `image` | string | yes |  | The image's key in the batch (batch_status or get_batch: key). |
| `measurement` | object | yes |  | {a_x, a_y, b_x, b_y, length_px, length_um, pixconv, label?, type?}: a line's ends in MATLAB axes and its length. |

## update_measurement

Its new ends, length, label and type.

|  |  |
|---|---|
| Route | [`POST /api/ais/measurements/{measurement_id}/update`](api.md#post-apiaismeasurementsmeasurement_idupdate) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `expect` | integer | no | at least 0 | The rev you last saw (optional). If someone changed it since, the call is refused with the current one. |
| `measurement` | object | yes |  | {a_x, a_y, b_x, b_y, length_px, length_um, pixconv, label?, type?}: a line's ends in MATLAB axes and its length. |
| `measurement_id` | integer | yes | at least 1 | The recorded line's id, from list_measurements. |

## delete_measurement

Cannot be undone.

|  |  |
|---|---|
| Route | [`POST /api/ais/measurements/{measurement_id}/delete`](api.md#post-apiaismeasurementsmeasurement_iddelete) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `expect` | integer | no | at least 0 | The rev you last saw (optional). If someone changed it since, the call is refused with the current one. |
| `measurement_id` | integer | yes | at least 1 | The recorded line's id, from list_measurements. |

## set_measure_types

The team's new list of types: names.

|  |  |
|---|---|
| Route | [`POST /api/ais/measure-types`](api.md#post-apiaismeasure-types) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `types` | array of string | yes |  |  |

## reset_batch_auto

Deletes every AIS auto mode saved on the batch (the rest renumbered) and the done marks of the images they were on, to run auto again. What went is kept in the Batches screen's Trash for 30 days, where a person can put it back.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/reset`](api.md#post-apiaisbatchesbatch_idreset) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |

## auto_defaults

What an auto run or detect_image uses unless told otherwise, and what may be set: general (methods, filters), settings (the method's), threshold, engines, z_methods.

|  |  |
|---|---|
| Route | [`GET /api/ais/auto/defaults`](api.md#get-apiaisautodefaults) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|

## start_auto_run

Auto mode over a whole batch, run by the server: every included image (less the complete ones unless skip_done: false), each AIS the filters keep saved straight to the batch, as the browser's review 'all'. Answers at once; follow it with get_auto_run. mark_done also marks each image done. images: only these keys.

|  |  |
|---|---|
| Route | [`POST /api/ais/batches/{batch_id}/auto`](api.md#post-apiaisbatchesbatch_idauto) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `engine` | string or null | no | one of `fast`, `null` | fast: Settings' Method 'ais_auto.m (fast)', the same answer, sooner. |
| `general` | object | no |  | Settings' general auto mode fields (see auto_defaults), e.g. {auto_method: 'fitted', fitted_min_length: 13}. Left out: the defaults. |
| `images` | array of string | no |  |  |
| `mark_done` | boolean | no |  |  |
| `settings` | object | no |  | The method settings (see auto_defaults: settings), e.g. {pixconv: 0.161}. Left out: the defaults. |
| `skip_done` | boolean | no |  |  |
| `threshold` | number | no | 0 to 1 | Default 0.01 (0 = Otsu). |

## get_auto_run

How far a run has got: state (queued, running, finished, stopped, failed), done/total images, found, hidden, saved, errors per image.

|  |  |
|---|---|
| Route | [`GET /api/ais/auto/{run_id}`](api.md#get-apiaisautorun_id) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `run_id` | string | yes |  |  |

## list_auto_runs

The server's auto runs since it started, newest first; batch_id narrows them.

|  |  |
|---|---|
| Route | [`GET /api/ais/auto`](api.md#get-apiaisauto) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | no | at least 1 | The batch's id, from list_batches. |

## cancel_auto_run

Stops after the image it is on; what it saved stays. Whoever started it, or an admin.

|  |  |
|---|---|
| Route | [`POST /api/ais/auto/{run_id}/cancel`](api.md#post-apiaisautorun_idcancel) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `run_id` | string | yes |  |  |

## export_report

The Batches screen's report (report.xlsx) as JSON sheets -- summary, images, assignees, ais, measurements, measurement_types, and for admins original_names, by_treatment, statistics -- each {columns, rows}. batch: one id, several separated by commas, or all. Left-out images only with everything. unblind (admins): blinded images under their original names. sheets narrows it to those.

|  |  |
|---|---|
| Route | [`GET /api/ais/report`](api.md#get-apiaisreport) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch` | string | yes |  | A batch id, ids separated by commas, or all. |
| `everything` | boolean | no |  |  |
| `sheets` | string | no |  | Sheet names separated by commas. |
| `unblind` | boolean | no |  |  |

## compare_batches

The comparison export (comparison.xlsx) as JSON: per measure the culture means, the treatment summary, every test with Holm-corrected p and stars, all values and original names, each sheet {columns, rows}; plus the raw groups, pooled, stats. Two batches or more (one culture each) for the tests between cultures. tests: anova, tukey, welch, dunnett, twoway, paired, unpaired, ks; units: culture means, individual values (every one when left out; nothing is averaged per image: each AIS of a treatment within a culture counts alike, and each culture is one n). design: the two-way ANOVA's factors, "drug x add-on" (default) or "treatment x culture". plots: true adds the box and cumulative plots as SVG.

|  |  |
|---|---|
| Route | [`POST /api/ais/compare`](api.md#post-apiaiscompare) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_ids` | array of integer | yes |  |  |
| `design` | string | no | one of `drug x add-on`, `treatment x culture` |  |
| `labels` | object | no |  | {measure id: name} for the plots' titles. |
| `plots` | boolean | no |  |  |
| `tests` | array of string | no |  |  |
| `units` | array of string | no |  |  |

## archive_batch_bulk

Runs archive_batch once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/ais/batches/archive`](api.md#post-apibulkaisbatchesarchive) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].archived` | boolean | no |  |  |
| `items[].batch_id` | integer | yes | at least 1 |  |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |
| `shared.archived` | boolean | no |  |  |

## set_image_done_bulk

Runs set_image_done once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/ais/batches/done`](api.md#post-apibulkaisbatchesdone) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].batch_id` | integer | yes | at least 1 |  |
| `items[].done` | boolean | no |  |  |
| `items[].image` | string | no |  | The image's key. |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |
| `shared.done` | boolean | no |  |  |
| `shared.image` | string | no |  | The image's key. |

## assign_batch_bulk

Runs assign_batch once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/ais/batches/assign`](api.md#post-apibulkaisbatchesassign) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].batch_id` | integer | yes | at least 1 |  |
| `items[].shares` | array of object | no |  |  |
| `items[].shares[].percent` | number | yes |  | Above 0; the shares are scaled to sum 100. |
| `items[].shares[].user_id` | integer | yes |  |  |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |
| `shared.shares` | array of object | no |  |  |
| `shared.shares[].percent` | number | yes |  | Above 0; the shares are scaled to sum 100. |
| `shared.shares[].user_id` | integer | yes |  |  |

## update_result_bulk

Runs update_result once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/ais/results/update`](api.md#post-apibulkaisresultsupdate) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].expect` | integer | no | at least 0 | The rev you last saw. Answers 409, with the record as it is now, if it has moved on. |
| `items[].result_id` | integer | yes |  |  |
| `items[].row` | object | no |  | The new trace's numbers, texts and pixels, as POST /api/ais/trace gives them. |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |
| `shared.expect` | integer | no | at least 0 | The rev you last saw. Answers 409, with the record as it is now, if it has moved on. |
| `shared.row` | object | no |  | The new trace's numbers, texts and pixels, as POST /api/ais/trace gives them. |

## delete_result_bulk

Runs delete_result once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/ais/results/delete`](api.md#post-apibulkaisresultsdelete) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].expect` | integer | no | at least 0 | The rev you last saw. Answers 409, with the record as it is now, if it has moved on. |
| `items[].result_id` | integer | yes |  |  |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |
| `shared.expect` | integer | no | at least 0 | The rev you last saw. Answers 409, with the record as it is now, if it has moved on. |

## update_measurement_bulk

Runs update_measurement once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/ais/measurements/update`](api.md#post-apibulkaismeasurementsupdate) |
| Read only | no |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].expect` | integer | no | at least 0 | The rev you last saw. Answers 409, with the record as it is now, if it has moved on. |
| `items[].measurement` | object | no |  |  |
| `items[].measurement.a_x` | number | yes |  |  |
| `items[].measurement.a_y` | number | yes |  |  |
| `items[].measurement.b_x` | number | yes |  |  |
| `items[].measurement.b_y` | number | yes |  |  |
| `items[].measurement.label` | string | no |  |  |
| `items[].measurement.length_px` | number | yes |  |  |
| `items[].measurement.length_um` | number | yes |  |  |
| `items[].measurement.pixconv` | number | yes |  |  |
| `items[].measurement.type` | string | no |  | One of the team's measurement types, or empty. |
| `items[].measurement_id` | integer | yes |  |  |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |
| `shared.expect` | integer | no | at least 0 | The rev you last saw. Answers 409, with the record as it is now, if it has moved on. |
| `shared.measurement` | object | no |  |  |
| `shared.measurement.a_x` | number | yes |  |  |
| `shared.measurement.a_y` | number | yes |  |  |
| `shared.measurement.b_x` | number | yes |  |  |
| `shared.measurement.b_y` | number | yes |  |  |
| `shared.measurement.label` | string | no |  |  |
| `shared.measurement.length_px` | number | yes |  |  |
| `shared.measurement.length_um` | number | yes |  |  |
| `shared.measurement.pixconv` | number | yes |  |  |
| `shared.measurement.type` | string | no |  | One of the team's measurement types, or empty. |

## delete_measurement_bulk

Runs delete_measurement once per item: items holds each call's arguments, shared the arguments they have in common (an item's own win). In order; one failing does not stop the rest, and the reply says how each went. At most 100 items.

|  |  |
|---|---|
| Route | [`POST /api/bulk/ais/measurements/delete`](api.md#post-apibulkaismeasurementsdelete) |
| Read only | no |
| Destructive | yes |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `items` | array of object | yes |  | One entry per thing to change: its id, and any field that differs from shared. |
| `items[].expect` | integer | no | at least 0 | The rev you last saw. Answers 409, with the record as it is now, if it has moved on. |
| `items[].measurement_id` | integer | yes |  |  |
| `shared` | object | no |  | Fields every item gets, unless the item sets its own. |
| `shared.expect` | integer | no | at least 0 | The rev you last saw. Answers 409, with the record as it is now, if it has moved on. |

## upload_instructions

Image bytes do not go through MCP: POST each file's raw bytes to the url given, with your API key (Content-Type: application/octet-stream). With batch_id, also the files that batch still needs (sha, name, rel, image).

|  |  |
|---|---|
| Route | [`POST /api/ais/files`](api.md#post-apiaisfiles) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | no | at least 1 | A batch: also list the files it still needs. |

## files_stored

For each sha-256, whether the server already holds that file (so it need not be uploaded again).

|  |  |
|---|---|
| Route | [`POST /api/ais/files`](api.md#post-apiaisfiles) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `shas` | array of string | yes |  | sha-256s, lower-case hex. |

## get_image

An image as PNG: the processed view the Process screen traces on (view), a thumbnail (thumb), or a .czi's channels together (composite).

|  |  |
|---|---|
| Route | [`GET /api/ais/files/{sha}/view.png`](api.md#get-apiaisfilesshaviewpng) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `kind` | string | no | one of `view`, `thumb`, `composite` | view (default): the processed image as the Process screen shows it; thumb: small; composite: a .czi's channels together. |
| `sha` | string | yes |  | The file's sha (get_batch: images[].files[role].sha). |

## trace_click

What a click on the Process screen does: the AIS traced from that point, with the row to save (save_result) when it worked. Uses the auto_defaults settings unless given.

|  |  |
|---|---|
| Route | [`POST /api/ais/trace`](api.md#post-apiaistrace) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `click` | array of number | yes |  | [x, y] in MATLAB axes: x = column, y = row, pixel centres at 1..n. |
| `click2` | array of number | no |  | The second click after re-thresholding; default the first again. |
| `engine` | string or null | no | one of `fast`, `null` | fast: Settings' Method 'ais_auto.m (fast)', the same answer, sooner. |
| `image` | string | yes |  | The image's key in the batch (batch_status or get_batch: key). |
| `settings` | object | no |  | The method settings (see auto_defaults: settings), e.g. {pixconv: 0.161}. Left out: the defaults. |
| `threshold` | number | no | 0 to 1 | Default 0.01 (0 = Otsu). |
| `z_method` | string | no |  | A Z-stack's method (default trace_lift). |

## detect_image

Auto mode on one image without saving: every candidate the filters keep (include_hidden: the rest too), each with passes and the row save_result takes -- so you can review and save them yourself. The image's saved AIS are left out of the search.

|  |  |
|---|---|
| Route | [`POST /api/ais/detect`](api.md#post-apiaisdetect) |
| Read only | yes |
| Destructive | no |

**Arguments**

| Field | Type | Required | Limits | Description |
|---|---|---|---|---|
| `batch_id` | integer | yes | at least 1 | The batch's id, from list_batches. |
| `engine` | string or null | no | one of `fast`, `null` | fast: Settings' Method 'ais_auto.m (fast)', the same answer, sooner. |
| `general` | object | no |  | Settings' general auto mode fields (see auto_defaults), e.g. {auto_method: 'fitted', fitted_min_length: 13}. Left out: the defaults. |
| `image` | string | yes |  | The image's key in the batch (batch_status or get_batch: key). |
| `include_hidden` | boolean | no |  | Also list the candidates the filters leave out (default false). |
| `settings` | object | no |  | The method settings (see auto_defaults: settings), e.g. {pixconv: 0.161}. Left out: the defaults. |
| `threshold` | number | no | 0 to 1 | Default 0.01 (0 = Otsu). |
| `verbose` | boolean | no |  | Keep each candidate's whole trace data (path, spline, profile, component). Default false. |

## HTTP only

Routes an API key may call that have no tool, and why.

| Route | Why |
|---|---|
| [`GET /api/about/report`](api.md#get-apiaboutreport) | The About screen's copy of a document in the repository; nothing to act on. |
| [`GET /api/admin/users/{user_id}/keys`](api.md#get-apiadminusersuser_idkeys) | Manages API keys, which no MCP tool does. |
| [`GET /api/ais/files/{sha}/channel/{index}.png`](api.md#get-apiaisfilesshachannelindexpng) | Viewer images for the Process screen; get_image gives an agent the processed view. |
| [`GET /api/ais/files/{sha}/channel/{index}.tif`](api.md#get-apiaisfilesshachannelindextif) | File bytes: MCP messages are JSON, and clients cap their size. Fetch it over HTTP with the same key. |
| [`GET /api/ais/files/{sha}/channels`](api.md#get-apiaisfilesshachannels) | Viewer detail for the Process screen's channel picker; get_batch names each image's files. |
| [`GET /api/ais/files/{sha}/composite.png`](api.md#get-apiaisfilesshacompositepng) | Reached through get_image with kind composite. |
| [`GET /api/ais/files/{sha}/file`](api.md#get-apiaisfilesshafile) | File bytes: MCP messages are JSON, and clients cap their size. Fetch it over HTTP with the same key. |
| [`GET /api/ais/files/{sha}/processed.tif`](api.md#get-apiaisfilesshaprocessedtif) | File bytes: MCP messages are JSON, and clients cap their size. Fetch it over HTTP with the same key. |
| [`GET /api/ais/files/{sha}/slice/{index}.png`](api.md#get-apiaisfilesshasliceindexpng) | Viewer images for the Process screen's z-stack slider; get_image gives an agent the processed view. |
| [`GET /api/ais/files/{sha}/somata`](api.md#get-apiaisfilesshasomata) | Viewer overlay for the Process screen; detect_image and trace_click give an agent the results. |
| [`GET /api/ais/files/{sha}/thumb.png`](api.md#get-apiaisfilesshathumbpng) | Reached through get_image with kind thumb. |
| [`GET /api/ais/local/status`](api.md#get-apiaislocalstatus) | Whether Open path and MATLAB work on this machine: those routes need a browser session. |
| [`GET /api/ais/matlab/helper/download/{platform}`](api.md#get-apiaismatlabhelperdownloadplatform) | The MATLAB helper program itself, a download for a person's computer. |
| [`GET /api/ais/matlab/helper/jobs/{job_id}/bundle`](api.md#get-apiaismatlabhelperjobsjob_idbundle) | Called by the MATLAB helper program, not by agents; the bundle is a zip. |
| [`GET /api/ais/matlab/helper/next`](api.md#get-apiaismatlabhelpernext) | Called by the MATLAB helper program, not by agents. |
| [`GET /api/ais/trash`](api.md#get-apiaistrash) | The trash only holds what the Batches screen deleted, which agents cannot do. |
| [`GET /api/api.json`](api.md#get-apiapijson) | The API reference itself; GET /api/mcp.json is the MCP one. |
| [`GET /api/api.md`](api.md#get-apiapimd) | The API reference itself, for people; GET /api/api.json is the same as JSON. |
| [`GET /api/mcp.json`](api.md#get-apimcpjson) | The MCP reference itself; tools/list gives the same list. |
| [`GET /api/mcp.md`](api.md#get-apimcpmd) | The MCP reference itself, for people; tools/list gives the same list. |
| [`POST /api/admin/keys/{key_id}/revoke`](api.md#post-apiadminkeyskey_idrevoke) | Manages API keys, which no MCP tool does. |
| [`POST /api/admin/users/{user_id}/keys`](api.md#post-apiadminusersuser_idkeys) | Makes an API key, which no MCP tool does. |
| [`POST /api/ais/batches/import`](api.md#post-apiaisbatchesimport) | A backup zip: MCP messages are JSON, and clients cap their size. Send it over HTTP with the same key. |
| [`POST /api/ais/batches/import/missing`](api.md#post-apiaisbatchesimportmissing) | A backup zip: MCP messages are JSON, and clients cap their size. Send it over HTTP with the same key. |
| [`POST /api/ais/batches/{batch_id}/activity`](api.md#post-apiaisbatchesbatch_idactivity) | The Process screen reporting that someone is working on a batch, not an action. |
| [`POST /api/ais/batches/{batch_id}/delete`](api.md#post-apiaisbatchesbatch_iddelete) | Deleting a whole batch is kept out of agents' reach on purpose. |
| [`POST /api/ais/files/{sha}/pair`](api.md#post-apiaisfilesshapair) | A first guess for the Measure tool on the Process screen; it stores nothing. |
| [`POST /api/ais/folders/{folder_id}/delete`](api.md#post-apiaisfoldersfolder_iddelete) | Deleting a folder is kept out of agents' reach on purpose. |
| [`POST /api/ais/matlab/bundle`](api.md#post-apiaismatlabbundle) | A MATLAB run as a zip download for a person's computer. |
| [`POST /api/ais/matlab/helper/jobs/{job_id}/done`](api.md#post-apiaismatlabhelperjobsjob_iddone) | Called by the MATLAB helper program, not by agents. |
| [`POST /api/ais/results/import`](api.md#post-apiaisresultsimport) | A results file upload: MCP messages are JSON, and clients cap their size. Send it over HTTP with the same key. |
| [`POST /api/ais/trash/{trash_id}/purge`](api.md#post-apiaistrashtrash_idpurge) | Deleting for good is kept out of agents' reach on purpose. |
| [`POST /api/ais/trash/{trash_id}/restore`](api.md#post-apiaistrashtrash_idrestore) | The trash only holds what the Batches screen deleted, which agents cannot do. |
| [`POST /api/bulk/ais/batches/delete`](api.md#post-apibulkaisbatchesdelete) | Deleting a whole batch is kept out of agents' reach on purpose. |
| [`POST /api/bulk/ais/batches/reset`](api.md#post-apibulkaisbatchesreset) | Resetting many batches at once, all results included, is kept out of agents' reach on purpose. |
| [`POST /api/bulk/ais/trash/purge`](api.md#post-apibulkaistrashpurge) | Deleting for good is kept out of agents' reach on purpose. |
| [`POST /api/bulk/ais/trash/restore`](api.md#post-apibulkaistrashrestore) | The trash only holds what the Batches screen deleted, which agents cannot do. |
| [`POST /api/logout`](api.md#post-apilogout) | Ends a browser session; a key has none to end. |
| [`POST /api/logs/events`](api.md#post-apilogsevents) | The browser's own activity reports (track.js), not an action. |
| [`POST /mcp`](api.md#post-mcp) | The MCP endpoint itself. |
