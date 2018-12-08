from .day05_pt1 import reactor


def test_reactor():
    polymer = 'dabAcCaCBAcCcaDA'
    assert reactor(polymer) == 'dabCBAcaDA'
