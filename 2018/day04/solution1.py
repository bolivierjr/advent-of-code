import os
from typing import List, Tuple


directory: str = os.path.dirname(os.path.abspath(__file__))
filename: str = os.path.join(directory, 'input.txt')

with open(filename, 'r') as fp:
    logs: List[str] = sorted(fp.read().splitlines())


def find_most_sleepy(data: List[str]) -> Tuple[str, int]:
    queue: list = []
    guards: dict = {}
    sleep = 0

    for log in logs:
        raw_datetime, description = log.split(']')
        _, time = raw_datetime.split()
        _, minute = time.split(':')

        if 'Guard' in description:
            _, guard, _, _ = description.split()

            if guard not in guards:
                guards[guard] = 0
            if queue:
                queue.pop()
            queue.append(guard)
            continue

        guard_queue = queue[0]

        if guards and 'falls' in description:
            sleep += int(minute)
        elif guards and 'wakes' in description:
            sleep = int(minute) - sleep
            guards[guard_queue] = sleep
            sleep = 0
    print(guards)
    return max(guards.items())


if __name__ == '__main__':
    sleepy_guard: Tuple[str, int] = find_most_sleepy(logs)
    print(sleepy_guard)
