import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from scripts.import_atc_2025 import build_docs, parse_usenix_sessions


class ParseUsenixSessionsTests(unittest.TestCase):
    def test_extracts_authors_from_usenix_paper_field(self):
        html = """
        <article class="node-session">
          <h2>Cloud Computing</h2>
          <article class="node-paper">
            <h2><a href="/conference/atc25/presentation/example">Example</a></h2>
            <div class="field-name-field-paper-people-text">
              <p>Alice, <em>Example University;</em> Bob, <em>Example Lab</em></p>
            </div>
          </article>
        </article>
        """
        paper = parse_usenix_sessions(html)["Cloud Computing"][0]
        self.assertEqual(paper.authors, "Alice, Example University; Bob, Example Lab")

    def test_missing_authors_raises(self):
        html = """
        <article class="node-session">
          <h2>Cloud Computing</h2>
          <article class="node-paper">
            <h2><a href="/conference/atc25/presentation/example">Example</a></h2>
          </article>
        </article>
        """
        with self.assertRaisesRegex(ValueError, "Missing authors for paper: Example"):
            parse_usenix_sessions(html)

    def test_existing_conference_content_is_preserved(self):
        with TemporaryDirectory() as tmp:
            docs = Path(tmp)
            existing = docs / "ATC" / "2025" / "index.md"
            existing.parent.mkdir(parents=True)
            existing.write_text("Existing content")
            with patch("scripts.import_atc_2025.DOCS", docs):
                with self.assertRaisesRegex(FileExistsError, "Refusing to overwrite"):
                    build_docs({})
            self.assertEqual(existing.read_text(), "Existing content")


if __name__ == "__main__":
    unittest.main()
