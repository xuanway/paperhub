import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from scripts.import_eurosys_2025 import build_docs, main, replace_nav


class EuroSysImporterSafetyTests(unittest.TestCase):
    def test_existing_content_is_preserved_without_fetching(self):
        with TemporaryDirectory() as tmp:
            docs = Path(tmp)
            existing = docs / "EuroSys" / "2025" / "index.md"
            existing.parent.mkdir(parents=True)
            existing.write_text("Existing content")
            with patch("scripts.import_eurosys_2025.DOCS", docs), patch("scripts.import_eurosys_2025.curl_fetch") as fetch:
                with self.assertRaisesRegex(FileExistsError, "Refusing to overwrite"):
                    main()
                with self.assertRaisesRegex(FileExistsError, "Refusing to overwrite"):
                    build_docs({})
                fetch.assert_not_called()
            self.assertEqual(existing.read_text(), "Existing content")

    def test_replace_only_target_year(self):
        source = (
            "nav:\n  - ⚙️ EuroSys:\n"
            "    - EuroSys 2026 (1):\n      - old 2026: EuroSys/2026/index.md\n"
            "    - EuroSys 2025 (1):\n      - old 2025: EuroSys/2025/index.md\n"
            "    - EuroSys 2024 (1):\n      - old 2024: EuroSys/2024/index.md\n"
            "  - Other: index.md\n"
        )
        new = ["    - EuroSys 2025 (2):\n", "      - EuroSys 2025: EuroSys/2025/index.md\n"]
        result = replace_nav(source, new)
        self.assertIn("old 2026: EuroSys/2026/index.md", result)
        self.assertIn("old 2024: EuroSys/2024/index.md", result)
        self.assertNotIn("old 2025", result)
        self.assertLess(result.index("EuroSys 2026"), result.index("EuroSys 2025"))
        self.assertLess(result.index("EuroSys 2025"), result.index("EuroSys 2024"))

    def test_insert_missing_year_in_descending_order(self):
        source = (
            "nav:\n  - ⚙️ EuroSys:\n"
            "    - EuroSys 2026 (1):\n      - EuroSys 2026: EuroSys/2026/index.md\n"
            "    - EuroSys 2024 (1):\n      - EuroSys 2024: EuroSys/2024/index.md\n"
            "  - Other: index.md\n"
        )
        result = replace_nav(source, ["    - EuroSys 2025 (2):\n"])
        self.assertLess(result.index("EuroSys 2026"), result.index("EuroSys 2025"))
        self.assertLess(result.index("EuroSys 2025"), result.index("EuroSys 2024"))
        self.assertIn("  - Other: index.md", result)


if __name__ == "__main__":
    unittest.main()
