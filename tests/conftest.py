import copy
import json
from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES


@pytest.fixture
def records() -> list[dict]:
    return json.loads((FIXTURES / "investors.json").read_text(encoding="utf-8"))


@pytest.fixture
def example(records) -> dict:
    return copy.deepcopy(records[0])
