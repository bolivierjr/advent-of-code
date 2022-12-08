#!/usr/bin/python
# -*- coding: utf-8 -*-

from part_1 import find_solution_one

test_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def test_find_solution_one():
    elf_number, total_calories = find_solution_one(test_data)
    assert 4 == elf_number
    assert 24000 == total_calories
