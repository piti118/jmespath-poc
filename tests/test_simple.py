import json
from os.path import dirname, join

from jmespath_poc import search
import pytest


@pytest.fixture
def database():
    with open(join(dirname(__file__), './fixtures/example.json')) as f:
        yield json.load(f)


def test_search(database):
    expr = '[*].map_merge({well_name: name}, chemical_uses[*].{chemical_name: name, amount: amount})[]'
    got = search(expr, database)
    assert len(got) == 60
    assert got[0]['well_name'] == '0fd36'
