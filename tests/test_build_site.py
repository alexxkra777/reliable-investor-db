import importlib.util
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("build_site", ROOT / "scripts/build_site.py")
build_site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_site)


def test_site_prefills_every_reviewed_claim(tmp_path):
    build_site.main(tmp_path)
    html = (tmp_path / "index.html").read_text(encoding="utf-8")

    claims = json.loads(re.search(r"var CLAIMS = (\[.*?\]);\n", html).group(1))
    reviewed = json.loads(re.search(r"var REVIEWED = (\{.*?\});\n", html).group(1))
    assert {c["claim_id"] for c in claims} == set(reviewed)
    assert sum(v["label"] == "correct" for v in reviewed.values()) == 58
    assert sum(v["label"] == "wrong" for v in reviewed.values()) == 2
    assert "58 correct" in html and "2 wrong" in html
    assert 'id="restore"' in html


def test_site_build_fails_loudly_when_page_changes():
    with pytest.raises(SystemExit):
        build_site.build("<html><body></body></html>", {})
