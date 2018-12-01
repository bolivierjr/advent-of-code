#!/usr/bin/env python3

import argparse
from typing import List, IO


class Input:
    def __init__(self, path: IO[str]):
        self.data = []
        with open(path, 'r') as fp:
            for line in fp:
                self.data.append(line)


class Frequency:
    def __init__(self, data: List[str]):
        self._data = data

    @property
    def result(self) -> int:
        frequency: int = 0

        for adjustment in self._data:
            adjustment = adjustment.replace('\n', '')
            frequency += int(adjustment)

        return frequency


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get the result from an input'
                                     'file for adventofcode puzzles')
    parser.add_argument('-s', '--source', help='the path to the input file',
                        required=True)
    args = parser.parse_args()

    file = Input(args.source)
    frequency = Frequency(file.data)

    print(f'The end frequency is {frequency.result}.')
