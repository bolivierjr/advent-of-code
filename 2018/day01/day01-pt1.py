#!/usr/bin/env python3

import argparse
from typing import List, IO


class Input:
    def __init__(self, path: IO[str]):
        self._data = []
        with open(path, 'r') as fp:
            for line in fp:
                self._data.append(line)

    @property
    def input(self) -> List[str]:
        return self._data


class Frequency:
    def __init__(self, data: List[str]):
        self._data = data

    @property
    def result(self) -> int:
        frequency: int = 0

        for item in self._data:
            item = item.replace('\n', '')

            if item.startswith('+'):
                frequency += int(item[1:])
            else:
                frequency -= int(item[1:])

        return frequency


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get the result from an input'
                                     'file for adventofcode puzzles')
    parser.add_argument('-s', '--source', help='the path to the input file',
                        required=True)
    args = parser.parse_args()

    file = Input(args.source)
    frequency = Frequency(file.input)

    print(f'The end frequency is {frequency.result}.')
