import os
from typing import Dict, List, Deque
from collections import deque, Counter


def get_data() -> List[Dict[str, int]]:
    directory: str = os.path.dirname(os.path.abspath(__file__))
    filename: str = os.path.join(directory, 'input.txt')
    data: List[dict] = []

    with open(filename, 'r') as fp:
        for line in fp:
            column2: List[str] = line.split(' ')[2].split(',')
            column3: List[str] = line.split(' ')[3].split('x')

            specs: Dict[str, int] = {
                'left': int(column2[0]),
                'top': int(column2[1].rstrip(':')),
                'width': int(column3[0]),
                'height': int(column3[1].rstrip('\n'))
            }

            data.append(specs)

    return data


if __name__ == '__main__':
    data = get_data()
    fabrics = deque()

    for specs in data:
        for x in range(specs['width']):
            pass

            for y in range(specs['height']):
                x_coord = specs['left'] + x
                y_coord = -specs['top'] + -y
                fabrics.append((x_coord, y_coord))

    overlap = len([x for x in Counter(fabrics).values() if x > 1])

    print(f'Overlap: {overlap}')
