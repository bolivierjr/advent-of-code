#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from typing import Dict, Tuple


def find_solution_one(data: str) -> Tuple[int, int]:
    total_calories_per_elf = format_data_by_total_calories_per_elf(data)
    elf_with_most_calories: int = max(total_calories_per_elf, key=total_calories_per_elf.get)
    total_calories = total_calories_per_elf.get(elf_with_most_calories, 0)

    return elf_with_most_calories, total_calories


def find_solution_two(data: str) -> int:
    total_calories_per_elf = format_data_by_total_calories_per_elf(data)
    sorted_total_calories_list = sorted(total_calories_per_elf.values(), reverse=True)
    # top 3 calories from the elves with the most food in desc order
    top_three_most_calories = sorted_total_calories_list[0:3]
    sum_of_top_three_calories = sum(top_three_most_calories)

    return sum_of_top_three_calories


def format_data_by_total_calories_per_elf(data: str) -> Dict[int, int]:
    total_calories_per_elf: Dict[int, int] = {}

    for (elf, food) in enumerate(data.split("\n\n")):
        elf_number = elf + 1
        total_calories = sum(map(lambda calories: int(calories), food.split("\n")))
        total_calories_per_elf[elf_number] = total_calories

    return total_calories_per_elf


if __name__ == "__main__":
    directory: str = os.path.dirname(os.path.abspath(__file__))
    filename: str = os.path.join(directory, "input.txt")

    with open(filename, "r", encoding="utf-8") as fp:
        data: str = fp.read()

    start_time = time.time()
    elf_number, total_calories = find_solution_one(data)
    end_time = time.time()

    print(f"Part 1 Solution: Total calories are {total_calories} from elf {elf_number}.")
    print(f"Part 1 total time of execution: {(end_time - start_time) * 1000} ms")

    start_time = time.time()
    sum_of_total_calories = find_solution_two(data)
    end_time = time.time()

    print(f"Part 2 Solution: Total calories from the top three elves are {sum_of_total_calories}.")
    print(f"Part 2 total time of execution: {(end_time - start_time) * 1000} ms")
