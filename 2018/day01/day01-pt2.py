#!/usr/bin/env python3

import os
from typing import List, Set, IO


directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'input.txt')

with open(filename, 'r') as fp:
    data = fp.read().split()


class Frequency:
    def __init__(self, data: List[str]):
        self._data = data

    @property
    def result(self) -> int:
        frequency: int = 0
        freq_record: Set[int] = set()

        while True:
            for adjustment in self._data:
                frequency += int(adjustment)

                if frequency in freq_record:
                    return frequency
                else:
                    freq_record.add(frequency)


if __name__ == "__main__":
    frequency = Frequency(data)
    print(f'The first duplicate frequency is {frequency.result}.')
