"""MkDocs build hook: regenerate word cloud data before each build."""

import os
import subprocess
import sys


def on_pre_build(config):
    here = os.path.dirname(os.path.abspath(__file__))
    script = os.path.join(here, "gen_wordcloud_data.py")
    try:
        subprocess.run([sys.executable, script], check=True)
    except Exception as exc:
        print(f"Warning: word cloud data generation failed: {exc}", file=sys.stderr)
