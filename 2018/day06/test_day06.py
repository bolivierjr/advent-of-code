from .day06_pt1 import find_area

coords = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]


def test_find_area():
    assert find_area(coords) == 17
