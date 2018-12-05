import os
from typing import List, Tuple


directory: str = os.path.dirname(os.path.abspath(__file__))
filename: str = os.path.join(directory, 'input.txt')

with open(filename, 'r') as fp:
    data: List[str] = sorted(fp.read().splitlines())


def find_most_sleepy(logs: List[str]) -> Tuple[str, int]:
    queue = []
    guards = {}
    sleep = 0

    for log in logs:
        raw_datetime, description = log.split(']')
        _, time = raw_datetime.split()
        _, minute = time.split(':')
        guard_queue = queue[0]

        if 'Guard' in description:
            _, guard, _, _ = description.split()

            if guard not in guards:
                guards[guard] = []

            if queue:
                queue.pop()

            queue.append(guard)

        elif guards and 'falls' in description:
            sleep += int(minute)

        elif guards and 'wakes' in description:
            awake = int(minute) - sleep
            for x in range(sleep, awake + 1):
                pass

            guards[guard_queue] += sleep
            sleep, awake = 0, 0
    print(guards)
    return max(guards.items())


if __name__ == '__main__':
    find_most_sleepy(data)
    print(data)
