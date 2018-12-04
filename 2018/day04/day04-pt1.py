import os
from typing import Set


def get_sorted_data() -> Set[str]:
    directory: str = os.path.dirname(os.path.abspath(__file__))
    filename: str = os.path.join(directory, 'input.txt')
    data: Set[str] = set()

    with open(filename, 'r') as fp:
        for line in fp:
            data.add(line)

    return sorted(data)


if __name__ == '__main__':
    data: Set[str] = get_sorted_data()

    for item in data:
        time = item.split(']')[0].lstrip('[')
        log = item.split(']')[1].rstrip('\n')

    print(data)
