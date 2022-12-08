#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from typing import Dict, Tuple


def find_solution_one(data: str) -> Tuple[int, int]:
    food_per_elf = format_data_by_food_per_elf(data)
    elf_with_most_calories = find_elf_with_most_calories(food_per_elf)
    total_calories = food_per_elf.get(elf_with_most_calories, 0)

    return elf_with_most_calories, total_calories


def find_elf_with_most_calories(food_per_elf: Dict[int, int]) -> int:
    elf_with_most_calories = max(food_per_elf, key=food_per_elf.get)

    return elf_with_most_calories


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
        elf_number, total_calories = find_solution_one(data)

        print(f"Total calories are {total_calories} from elf {elf_number}.")
