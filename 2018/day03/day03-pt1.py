import os
from typing import Dict, List, Deque
from collections import deque


def get_data() -> List[Dict[str, str]]:
    directory: str = os.path.dirname(os.path.abspath(__file__))
    filename: str = os.path.join(directory, 'input.txt')
    data: List[dict] = []

    with open(filename, 'r') as fp:
        for line in fp:
            column0: List[str] = line.split(' ')[0]
            column2: List[str] = line.split(' ')[2].split(',')
            column3: List[str] = line.split(' ')[3].split('x')

            specs: Dict[str, str] = {
                'claim': column0,
                'left': column2[0],
                'top': column2[1].rstrip(':'),
                'width': column3[0],
                'height': column3[1].rstrip('\n')
            }

            data.append(specs)

    return data


if __name__ == '__main__':
    data = get_data()
    fabric = deque()

    for specs in data:
        pass
