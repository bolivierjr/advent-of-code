from .day05_pt1 import reactors


def test_reactor():
    polymer = 'dabAcCaCBAcCcaDA'
    assert reactors(polymer) == 'dabCBAcaDA'
