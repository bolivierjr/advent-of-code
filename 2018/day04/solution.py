import os
from typing import Dict, List, Tuple
from collections import Counter


directory: str = os.path.dirname(os.path.abspath(__file__))
filename: str = os.path.join(directory, 'input.txt')

with open(filename, 'r') as fp:
    data: List[str] = sorted(fp.read().splitlines())


def find_most_sleepy(guards: dict) -> Tuple[str, int]:
    nodders = set()

    for guard in guards:
        total_asleep = sum(guards[guard].values())
        nodders.add((guard, total_asleep))

    return max(nodders)


def get_sleepy_heads(logs: List[str]) -> Tuple[str, int]:
    queue = []
    guards = {}
    sleep = 0

    for log in logs:
        raw_datetime, description = log.split(']')
        _, time = raw_datetime.split()
        _, minute = time.split(':')

        if 'Guard' in description:
            _, guard, _, _ = description.split()

            if guard not in guards:
                guards[guard] = Counter()

            if queue:
                queue.pop()

            queue.append(guard)

        elif guards and 'falls' in description:
            sleep += int(minute)

        elif guards and 'wakes' in description:
            awake = int(minute) - sleep

            for number in range(sleep, awake + 1):
                guards[queue[0]].update(str(number))

            sleep = 0, 0

    sleeping_beauty = find_most_sleepy(guards)

    return sleeping_beauty


if __name__ == '__main__':
    get_sleepy_heads(data)
