import os
from queue import Queue
from typing import Union, List, Tuple, Dict, Set


class Planet:
    def __init__(self, name: str):
        self.name = name
        self.parent: Union[Planet, None] = None

    def count_orbits(self) -> int:
        if self.parent is None:
            return 0
        return 1 + self.parent.count_orbits()

    def path_to_com(self) -> Set[object]:
        distance = set()
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            distance.add(current_node)

            if current_node.parent:
                queue.put(current_node.parent)

        return distance


def make_system(orbits: List[Tuple[str, str]]) -> Dict[str, Planet]:
    orbital_system = {}
    for parent, child in orbits:
        parent_node: Planet
        child_node: Planet

        if parent in orbital_system:
            parent_node = orbital_system[parent]
        else:
            parent_node = Planet(parent)
            orbital_system[parent] = parent_node

        if child in orbital_system:
            child_node = orbital_system[child]
            child_node.parent = parent_node
        else:
            child_node = Planet(child)
            child_node.parent = parent_node
            orbital_system[child] = child_node

    return orbital_system


def total_orbits(orbital_system: Dict[str, Planet]) -> int:
    totals = [planet.count_orbits() for planet in orbital_system.values()]
    return sum(totals)


def get_distance(distance1: Set[Planet], distance2: Set[Planet]) -> int:
    common_paths = distance1 & distance2
    sorted_paths = list(sorted(common_paths, key=lambda x: x.path_to_com()))
    last_common_path = sorted_paths[-1].path_to_com()
    distance_last_common1 = len(distance1) - len(last_common_path)
    distance_last_common2 = len(distance2) - len(last_common_path)

    return distance_last_common1 + distance_last_common2 - 2


if __name__ == "__main__":
    directory: str = os.path.dirname(os.path.abspath(__file__))
    filename: str = os.path.join(directory, "input.txt")

    with open(filename, "r", encoding="utf-8") as fp:
        data: List[str] = fp.read().split()

    orbits = [tuple(row.split(")")) for row in data]
    orbital_system = make_system(orbits)
    total = total_orbits(orbital_system)

    you_route: Set[Planet] = orbital_system["YOU"].path_to_com()
    santa_route: Set[Planet] = orbital_system["SAN"].path_to_com()
    distance = get_distance(you_route, santa_route)

    print(f"Path from you to santa is: {distance}")
    print(f"Total orbits is: {total}")
