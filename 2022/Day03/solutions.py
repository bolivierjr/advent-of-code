#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import string
from typing import List, Tuple

LOWER_ALPHA = string.ascii_lowercase
UPPER_ALPHA = string.ascii_uppercase


def find_solution_one(data: str) -> int:
    rucksacks = process_data(data)
    duplicate_types = find_duplicate_item_types(rucksacks)
    sum_of_priorities = find_sum_of_priorities(duplicate_types)

    return sum_of_priorities


def process_data(data: str) -> List[Tuple[str, str]]:
    # formats rucksacks into [('vJrwpWtwJgWr', 'hcsFMMfFFhFp')]
    # a list of rucksacks with two compartments each
    return [(ruck[:len(ruck) // 2], ruck[len(ruck) // 2:]) for ruck in data.split("\n")]


def find_sum_of_priorities(duplicate_types: str):
    sum_of_priorities = 0

    for item_type in duplicate_types:
        found_type = False

        for lower_index, lower_letter in enumerate(LOWER_ALPHA):
            if item_type == lower_letter:
                found_type = True
                sum_of_priorities += lower_index + 1  # 1 through 26
                break

        if found_type:
            continue

        for upper_index, upper_letter in enumerate(UPPER_ALPHA):
            if item_type == upper_letter:
                sum_of_priorities += upper_index + 27  # 26 through 52
                break

    return sum_of_priorities


def find_duplicate_item_types(rucksacks: List[Tuple[str, str]]) -> str:
    duplicate_types = ''

    for compartment_one, compartment_two in rucksacks:
        for item_in_one in compartment_one:
            found_type = False

            for item_in_two in compartment_two:
                if item_in_one == item_in_two:
                    found_type = True
                    duplicate_types += item_in_one
                    break

            if found_type:
                break

    return duplicate_types


if __name__ == "__main__":
    directory: str = os.path.dirname(os.path.abspath(__file__))
    filename: str = os.path.join(directory, "input.txt")

    try:
        with open(filename, "r", encoding="utf-8") as fp:
            data: str = fp.read()
    except FileNotFoundError:
        print("Where is the file, idiot!?")
        sys.exit(1)

    start_time = time.perf_counter()
    my_score = find_solution_one(data)
    end_time = time.perf_counter()

    print(f"Part 1 score is {my_score}.")
    print( f"Part 1 total time of execution: {(end_time - start_time) * 1000} ms")
