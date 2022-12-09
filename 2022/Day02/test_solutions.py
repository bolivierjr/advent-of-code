#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from solutions import find_solution_one, find_solution_two


test_data = """A Y
B X
C Z"""


def test_find_solution_one():
    assert 15 == find_solution_one(test_data)


def test_find_solution_two():
    assert 12 == test_find_solution_two()
