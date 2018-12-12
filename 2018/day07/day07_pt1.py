#####################
# WIP: what a mess!
#####################

import os
import re
from typing import List
from string import ascii_uppercase
from collections import deque

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'input.txt')
with open(filename, 'r') as fp:
    instructions = fp.read()


def get_order(instructions: str) -> str:
    instructions = re.findall('[A-Z]\s', instructions)
    steps = deque(''.join(instructions).split())
    build_count = 0
    sleigh = ''

    while build_count < len(instructions):
        if steps[0] in steps[2]:
            sleigh += steps[0]
            steps.remove(steps.popleft())
            next_up = sorted([steps[0], steps[1]])

            if next_up[0] not in steps[0]:
                steps[0], steps[1] = steps[1], steps[0]

        steps += steps.popleft()
        build_count += 1


if __name__ == '__main__':
    tinstructions = 'Step C must be finished before step A can begin.\n'\
                    'Step C must be finished before step F can begin.\n'\
                    'Step A must be finished before step B can begin.\n'\
                    'Step A must be finished before step D can begin.\n'\
                    'Step B must be finished before step E can begin.\n'\
                    'Step D must be finished before step E can begin.\n'\
                    'Step F must be finished before step E can begin.\n'

    print(f'The result is {get_order(tinstructions)}')
