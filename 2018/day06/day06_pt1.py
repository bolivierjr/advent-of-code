#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from typing import List, Set, Tuple

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'input.txt')

coords = []
with open(filename, 'r') as fp:
    for line in fp:
        x, y = line.replace(',', '').split()
        coord = (int(x), int(y))
        coords.append((int(x), int(y)))


def get_distance(coord_1: tuple, coord_2: tuple) -> Tuple[int]:
    x1, y1 = coord_1
    x2, y2 = coord_2

    return abs(x1 - x2),  abs(y1 - y2)


def make_grid(coords: Set[tuple]) -> Set[tuple]:
    grid = set()
    coords.sort(key=lambda x: x[0])
    minimum, maximum = coords[0], coords[-1]
    x_distance, y_distance = get_distance(minimum, maximum)
    x_start, y_start = minimum
    x_end, x_end = maximum

    grid.add((minimum))
    for x in range(1, x_distance + 1):
        for y in range(1, y_distance + 1):
            grid.add((x_start + x, y))
            grid.add((x, y_start + y))

    grid.add((maximum))

    return grid


def find_area(coords: List[tuple]) -> int:
    grid = make_grid(coords)
    coords = set(coords)
    for coord in coords:
        pass


if __name__ == '__main__':
    tdata = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
    print(f'The size of the largest area is {find_area(coords)}')
