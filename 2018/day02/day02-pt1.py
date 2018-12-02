import os
import sys
from typing import Dict
from collections import Counter

directory: str = os.path.dirname(os.path.abspath(__file__))
filename: str = os.path.join(directory, 'input.txt')
two_count: int = 0
three_count: int = 0

with open(filename, 'r') as fp:
    for id_str in fp:
        char_count: Dict[str, int] = Counter(id_str)

        if 2 in char_count.values():
            two_count += 1

        if 3 in char_count.values():
            three_count += 1

print(f'checksum is {two_count * three_count}!')
