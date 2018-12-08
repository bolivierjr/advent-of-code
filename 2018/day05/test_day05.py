from .day05_pt1 import reactors
from .day05_pt2 import reactors2

polymer = 'dabAcCaCBAcCcaDA'


def test_reactor():
    assert reactors(polymer) == 'dabCBAcaDA'


def test_reactors2():
    assert reactors2(polymer) == 4
