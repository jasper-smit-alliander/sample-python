import pytest


@pytest.fixture
def input():
    return {"data": "testing"}


def test_sanity():
    assert 0 != 1


def test_input(input):
    assert input["data"] == "testing"
