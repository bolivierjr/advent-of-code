import os
from typing import Union, List, Tuple, Dict, Set
from queue import Queue

## **WIP**
class Planet:
    def __init__(self, name: str):
        self.name = name
        self.parent: Union[Planet, None] = None

    def count_orbits(self) -> int:
        if not self.parent:
            return 0
        return 1 + self.parent.count_orbits()

    def path_to_com(self) -> Set[object]:
        distance: Set[Planet] = {}
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

        if parent in orbital_system.keys():
            parent_node = orbital_system[parent]
        else:
            parent_node = Planet(parent)
            orbital_system[parent] = parent_node

        if child in orbital_system.keys():
            child_node = orbital_system[child]
            child_node.parent = parent_node
        else:
            child_node = Planet(child)
            child_node.parent = parent_node
            orbital_system[child] = child_node

    return orbital_system


def total_orbits(orbital_system: Dict[str, Planet]) -> int:
    totals = [planet.count_orbits() for planet in orbital_system.values()]
    return len(totals)


if __name__ == "__main__":
    directory: str = os.path.dirname(os.path.abspath(__file__))
    filename: str = os.path.join(directory, "input.txt")

    with open(filename, "r", encoding="utf-8") as fp:
        data: List[str] = fp.read().split()

    orbits = [tuple(row.split(")")) for row in data]
    orbital_system = make_system(orbits)
    total = total_orbits(orbital_system)
    print(f"Total orbits is: {total}")
