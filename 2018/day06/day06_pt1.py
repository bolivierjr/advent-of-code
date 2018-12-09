#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from typing import List, Set, Tuple, Dict
from collections import Counter

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
    min_coord, max_coord = coords[0], coords[-1]
    x_dist, y_dist = get_distance(min_coord, max_coord)
    x_start, y_start = min_coord
    x_end, y_end = max_coord

    grid.add((min_coord))
    for x in range(1, x_dist + 1):
        for y in range(1, y_dist + 1):
            grid.add((x + x_start, y))
            grid.add((x, y_start + y))

    grid.add((max_coord))

    return grid


def map_closest_coords(coords: list, grid: list) -> Dict[tuple, tuple]:
    closest_coords: Dict[tuple, tuple] = {}
    point_distances: Dict[tuple, int] = {}
    for point in grid:
        for iteration, coord in enumerate(coords):
            x_dist, y_dist = get_distance(point, coord)
            point_distances.update({coord: x_dist + y_dist})

            if iteration == len(coords) - 1:
                coord_counts = Counter(point_distances.values())
                minimum_dist_value = min(point_distances.values())
                minimum_dist_coord = min(
                    point_distances, key=point_distances.get)

                if coord_counts[minimum_dist_value] > 1:
                    closest_coords[point] = None
                else:
                    closest_coords[point] = minimum_dist_coord

                point_distances.clear()

    return closest_coords


def find_area(coords: List[tuple]) -> int:
    coords.sort(key=lambda x: x[0])
    grid = make_grid(coords)
    closest_coords = map_closest_coords(coords, grid)

    min_x, min_y = coords[0]
    max_x, max_y = coords[-1]
    for point, point_owner in closest_coords.items():
        pass


if __name__ == '__main__':
    tdata = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
    print(f'The size of the largest area is {find_area(tdata)}')
