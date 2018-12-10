import os
from typing import List
from string import ascii_uppercase
from collections import deque

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'input.txt')
with open(filename, 'r') as fp:
    instructions = fp.read()


def get_order(instructions: List[str]) -> str:
    instructions = instructions.split()
    a = deque()
    for instruction in instructions:
        if instruction in ascii_uppercase:
            a.add(instruction)


if __name__ == '__main__':
    print(f'The result is {get_order(tinstructions)}')
