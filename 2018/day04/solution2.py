import os
from typing import Dict, List, Tuple
from collections import Counter


directory: str = os.path.dirname(os.path.abspath(__file__))
filename: str = os.path.join(directory, 'input.txt')

with open(filename, 'r') as fp:
    data: List[str] = sorted(fp.read().splitlines())


def find_most_sleepy2(guards: dict) -> Tuple[str, int]:
    nodders = {}

    for guard, minutes in guards.items():
        most_common_min = Counter(minutes).most_common(1)
        if most_common_min:
            nodders.update({guard: most_common_min[0]})

    most_sleepy = max(nodders.keys(), key=(lambda x: nodders[x][1]))
    common_min, _ = nodders[most_sleepy]

    return most_sleepy, common_min


def get_sleepy_heads2(logs: List[str]) -> Tuple[str, int]:
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

    sleeping_beauty, common_min = find_most_sleepy2(guards)
    result = int(sleeping_beauty.lstrip('#')) * common_min

    return result


if __name__ == '__main__':
    result = get_sleepy_heads2(data)
    print(f'Solution2: {result}')
