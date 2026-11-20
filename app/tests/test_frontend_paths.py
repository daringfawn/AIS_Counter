"""URLs are paths (the python-webserver template's frontend rule 5): every
screen has a data-path, nothing routes by #hash, and no page URL carries a
?query (those belong to /api/ calls). The Process and Batches screens own the
paths under theirs too (data-subpaths), which the server answers with the app
page (StaticServer.serve_app_page)."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

STATIC = Path(__file__).resolve().parents[2] / "static"


def read(name: str) -> str:
    return (STATIC / name).read_text(encoding="utf-8")


def scripts() -> dict[str, str]:
    return {path.name: path.read_text(encoding="utf-8") for path in sorted((STATIC / "js").glob("*.js"))}


class FrontendPathsTest(unittest.TestCase):
    def test_urls_are_paths(self) -> None:
        html = read("index.html")
        sections = re.findall(r'<section\b[^>]*\bdata-view="[^"]*"[^>]*>', html)
        self.assertTrue(sections)
        for tag in sections:
            self.assertRegex(
                tag,
                r'data-path="/[a-z0-9-]+(/[a-z0-9-]+)*"',
                f"index.html: {tag} has no data-path. Every screen is a nested path like /admin/users",
            )
        paths = re.findall(r'data-path="([^"]*)"', html)
        self.assertEqual(len(paths), len(set(paths)), "index.html: two screens or cards share a data-path")

        sources = scripts()
        for page in sorted(STATIC.glob("*.html")):
            sources[page.name] = page.read_text(encoding="utf-8")
        for name, text in sources.items():
            for found in re.findall(r'href="#([^"]*)"', text):
                self.assertEqual(found, "main", f'{name}: href="#{found}" routes by hash. Link to the screen\'s path instead')
            self.assertNotIn("hashchange", text, f"{name} listens for hashchange. Screens are paths; listen for Nav's \"nav\" event")
            self.assertNotRegex(text, r"location\.hash\s*=[^=]", f"{name} sets location.hash. Screens are paths (Nav.go)")
            for url in re.findall(r'(?:location\.(?:replace|assign)\(\s*|location\.href\s*=\s*|href=)"([^"]*)"', text):
                if url.startswith("/api/") or "?" not in url:
                    continue
                self.fail(f"{name}: {url} puts a query on a page URL. Say it with a path, like /signed-out/ended")

    def test_deep_screens_have_server_routes(self) -> None:
        """A screen that owns the paths under its own needs a route that
        answers them with the app page, or a reload there is a 404."""
        from app.routes import build_routes
        from app.core.static_files import StaticServer

        deep = set(re.findall(r'<section\b[^>]*\bdata-path="(/[^"]*)"[^>]*\bdata-subpaths', read("index.html")))
        self.assertEqual(deep, {"/ais", "/batches"})
        table = {route.path: route for route in build_routes(StaticServer(STATIC)) if hasattr(route, "path")}
        self.assertIn("/ais/{rest:path}", table)
        self.assertIn("/batches/folder/{folder:int}", table)


if __name__ == "__main__":
    unittest.main()
