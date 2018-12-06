import os
from typing import Dict, List, Tuple
from collections import Counter


directory: str = os.path.dirname(os.path.abspath(__file__))
filename: str = os.path.join(directory, 'input.txt')

with open(filename, 'r') as fp:
    data: List[str] = sorted(fp.read().splitlines())


def find_most_sleepy(guards: dict) -> Tuple[str, int]:
    nodders = {}

    for guard, minutes in guards.items():
        total_asleep = sum(Counter(minutes).values())
        nodders.update({guard: total_asleep})

    _, most_sleepy = max(zip(nodders.values(), nodders.keys()))
    most_common_min = Counter(guards[most_sleepy]).most_common(1)[0][0]

    return most_sleepy, most_common_min


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
            awake = int(minute)

            for number in range(sleep, awake):
                guards[queue[0]].update({number: 1})

            sleep, awake = 0, 0

    sleeping_beauty, common_min = find_most_sleepy(guards)
    result = int(sleeping_beauty.lstrip('#')) * common_min

    return result


if __name__ == '__main__':
    result = get_sleepy_heads(data)
    print(f'Solution1: {result}')
