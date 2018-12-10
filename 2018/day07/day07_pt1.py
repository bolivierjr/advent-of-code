# WIP: what a mess!
#
#


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
    steps = []
    char_list = []
    for instruction in instructions:
        if instruction in ascii_uppercase:
            char_list.append(instruction)

        if char_list and len(char_list) % 8 == 0:
            if char_list[-4] in char_list[-2]:
                sort_nextstep = sorted([char_list[-3], char_list[-1]])
                steps.extend([char_list[0], sort_nextstep[0]])
                char_list = [char_list[-1]]
                char_list.extend(sort_list)
                a = 1


if __name__ == '__main__':
    tinstructions = 'Step C must be finished before step A can begin.\n'\
                    'Step C must be finished before step F can begin.\n'\
                    'Step A must be finished before step B can begin.\n'\
                    'Step A must be finished before step D can begin.\n'\
                    'Step B must be finished before step E can begin.\n'\
                    'Step D must be finished before step E can begin.\n'\
                    'Step F must be finished before step E can begin.\n'

    print(f'The result is {get_order(tinstructions)}')
