"""MkDocs build hook: regenerate word cloud data and patch nav counts before each build.

Key design: nav patching must happen in on_config — MkDocs parses mkdocs.yml into its
internal nav structure BEFORE on_pre_build fires, so any mkdocs.yml edits made during
on_pre_build are too late for the running build.  on_config runs while the config is
being loaded and the nav list is still the raw YAML structure (list of dicts), so we
can patch counts directly in memory here.
"""

import os
import sys
import re


def _get_stats():
    """Import and run generate() from gen_wordcloud_data.py; return stats dict."""
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, here)
    try:
        import gen_wordcloud_data as gwd
        # Force a fresh module reload so the DOCS_DIR path is correct
        import importlib
        importlib.reload(gwd)
        data = gwd.generate()
        return data.get("stats", {}) if data else {}
    except Exception as exc:
        print(f"Warning: word cloud data generation failed: {exc}", file=sys.stderr)
        return {}
    finally:
        if here in sys.path:
            sys.path.remove(here)


def _patch_nav_items(nav_items, per_track, conf_by_path):
    """Recursively patch (N) counts in the raw MkDocs nav list-of-dicts structure."""
    if not nav_items:
        return

    for item in nav_items:
        if not isinstance(item, dict):
            continue
        # Each nav item is a single-key dict: {label: path_or_list}
        keys = list(item.keys())
        for key in keys:
            value = item[key]
            if not isinstance(value, list):
                continue  # plain page link — skip

            # Identify the track/conf directory from the first index.md child
            track_dir = _find_index_dir(value)
            if track_dir:
                path_parts = track_dir.split("/")
                new_count = None
                if len(path_parts) == 3:
                    new_count = per_track.get(track_dir)
                elif len(path_parts) == 2:
                    new_count = conf_by_path.get(track_dir)

                if new_count is not None:
                    # Strip existing (N) suffix and add updated count
                    label_clean = re.sub(r"\s*\(\d+\+?\)\s*$", "", key).rstrip()
                    new_key = f"{label_clean} ({new_count})"
                    if new_key != key:
                        item[new_key] = item.pop(key)
                        value = item[new_key]

            # Recurse into children
            _patch_nav_items(value, per_track, conf_by_path)


def _find_index_dir(nav_list):
    """Return the directory of the first index.md page link found among direct children."""
    for child in nav_list:
        if not isinstance(child, dict):
            continue
        for v in child.values():
            if isinstance(v, str) and v.endswith("/index.md"):
                return os.path.dirname(v).replace("\\", "/")
            if isinstance(v, str) and v.endswith("index.md"):
                return os.path.dirname(v).replace("\\", "/")
    return None


def on_config(config):
    """Patch nav counts in-memory before MkDocs converts the nav YAML to objects."""
    stats = _get_stats()
    if not stats:
        return config

    per_track    = stats.get("per_track", {})
    per_conf_raw = stats.get("per_conf", {})   # {"HPCA 2025": {"total": 19, ...}}

    # Build conf_by_path: "HPCA/2025" -> 19
    conf_by_path = {}
    for conf_key, info in per_conf_raw.items():
        parts = conf_key.split()
        if len(parts) == 2:
            conf_by_path[f"{parts[0]}/{parts[1]}"] = info["total"]

    nav = config.get("nav")
    if nav:
        _patch_nav_items(nav, per_track, conf_by_path)

    return config
