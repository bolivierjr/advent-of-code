#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
from typing import Dict, Tuple


def find_solution_one(data: str) -> Tuple[int, int]:
    food_per_elf = format_data_by_food_per_elf(data)
    elf_with_most_calories: int = max(food_per_elf, key=food_per_elf.get)
    total_calories = food_per_elf.get(elf_with_most_calories, 0)

    return elf_with_most_calories, total_calories


def find_solution_two(data: str) -> int:
    food_per_elf = format_data_by_food_per_elf(data)
    sorted_total_calories_list = sorted(food_per_elf.values(), reverse=True)
    # top 3 calories from the elves with the most food in desc order
    top_three_most_calories = sorted_total_calories_list[0:3]
    sum_of_top_three_calories = sum(top_three_most_calories)

    return sum_of_top_three_calories


def format_data_by_food_per_elf(data: str) -> Dict[int, int]:
    # This ugly dictionary comprehension will format it like { 1: 10000, 2: 24000 }
    food_per_elf = {
        elf + 1: sum(map(lambda calories: int(calories), food.split("\n")))
        for (elf, food) in enumerate(data.split("\n\n"))
    }

    return food_per_elf


if __name__ == "__main__":
    directory: str = os.path.dirname(os.path.abspath(__file__))
    filename: str = os.path.join(directory, "input.txt")

    with open(filename, "r", encoding="utf-8") as fp:
        data: str = fp.read()

    start_time = time.time()
    elf_number, total_calories = find_solution_one(data)
    end_time = time.time()

    print(f"Part 1 Solution: Total calories are {total_calories} from elf {elf_number}.")
    print(f"Part 1 total time of execution: {end_time - start_time} seconds")

    start_time = time.time()
    total_calories = find_solution_two(data)
    end_time = time.time()

    print(f"Part 2 Solution: Total calories from the top three elves are {total_calories}.")
    print(f"Part 2 total time of execution: {end_time - start_time} seconds")
