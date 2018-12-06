import os
from typing import Dict, List, Tuple
from collections import Counter, deque


directory: str = os.path.dirname(os.path.abspath(__file__))
filename: str = os.path.join(directory, 'input.txt')

with open(filename, 'r') as fp:
    data: List[str] = sorted(fp.read().splitlines())


def find_most_sleepy(guards: dict) -> Tuple[str, int]:
    nodders1 = {}
    nodders2 = {}

    for guard, minutes in guards.items():
        total_asleep = sum(Counter(minutes).values())
        nodders1.update({guard: total_asleep})

        # most_common_min2, _ = Counter(minutes).most_common(1)[0]
        # nodders2.update({guard: most_common_min2})

    # _, most_sleepy = max(zip(nodders1.values(), nodders1.keys()))
    # most_common_min = Counter(guards[most_sleepy]).most_common(1)[0][0]

    # most_sleepy2 = max(zip(nodders2.keys(), nodders2.values()))

    # return most_sleepy, most_common_min, most_sleepy2


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

    # sleeping_beauty, common_min, most_sleepiest = find_most_sleepy(guards)
    # result = int(sleeping_beauty.lstrip('#')) * common_min

    # sleepybeauty2, common_min2 = most_sleepiest
    # result2 = int(sleepybeauty2.lstrip('#')) * common_min2

    # return result, result2


if __name__ == '__main__':
    pass
    result, result2 = get_sleepy_heads(data)
    print(f'Solution1: {result}')
    print(f'Solution 2: {result2}')
