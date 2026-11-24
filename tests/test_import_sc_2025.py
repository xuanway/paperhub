import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from scripts.import_sc_2025 import build_docs, main, replace_nav


class SCImporterSafetyTests(unittest.TestCase):
    def test_existing_content_is_preserved_without_fetching(self):
        with TemporaryDirectory() as tmp:
            docs = Path(tmp)
            existing = docs / "SC" / "2025" / "index.md"
            existing.parent.mkdir(parents=True)
            existing.write_text("Existing content")
            with patch("scripts.import_sc_2025.DOCS", docs), patch("scripts.import_sc_2025.curl_fetch") as fetch:
                with self.assertRaisesRegex(FileExistsError, "Refusing to overwrite"):
                    main()
                with self.assertRaisesRegex(FileExistsError, "Refusing to overwrite"):
                    build_docs({})
                fetch.assert_not_called()
            self.assertEqual(existing.read_text(), "Existing content")

    def test_replace_only_target_year(self):
        source = (
            "nav:\n  - 🌩️ SC:\n"
            "    - SC 2026 (1):\n      - old 2026: SC/2026/index.md\n"
            "    - SC 2025 (1):\n      - old 2025: SC/2025/index.md\n"
            "    - SC 2024 (1):\n      - old 2024: SC/2024/index.md\n"
            "  - Other: index.md\n"
        )
        new = ["    - SC 2025 (2):\n", "      - SC 2025: SC/2025/index.md\n"]
        result = replace_nav(source, new)
        self.assertIn("old 2026: SC/2026/index.md", result)
        self.assertIn("old 2024: SC/2024/index.md", result)
        self.assertNotIn("old 2025", result)
        self.assertLess(result.index("SC 2026"), result.index("SC 2025"))
        self.assertLess(result.index("SC 2025"), result.index("SC 2024"))

    def test_insert_missing_year_in_descending_order(self):
        source = (
            "nav:\n  - 🌩️ SC:\n"
            "    - SC 2026 (1):\n      - SC 2026: SC/2026/index.md\n"
            "    - SC 2024 (1):\n      - SC 2024: SC/2024/index.md\n"
            "  - Other: index.md\n"
        )
        result = replace_nav(source, ["    - SC 2025 (2):\n"])
        self.assertLess(result.index("SC 2026"), result.index("SC 2025"))
        self.assertLess(result.index("SC 2025"), result.index("SC 2024"))
        self.assertIn("  - Other: index.md", result)


if __name__ == "__main__":
    unittest.main()
