import os
import sys
from collections import Counter


PIXELS = 25 * 6
MAXINT = sys.maxsize


def get_lowest_digits(data: str) -> int:
    """
    Gets the lowest amount of zero digits in each image
    layer of data, then multiplies the number of one and
    two digits in that layer.

    Args:
        data (str): Long string of data from the input file.

    Returns:
        (int) The product of ones and twos left in the queue.
    """
    queue = [(MAXINT, 0)]
    while data:
        layer = data[0:PIXELS]
        counter = Counter(layer)

        zeros, ones, twos = counter["0"], counter["1"], counter["2"]
        zeros_queue, _ = queue[0]

        if zeros < zeros_queue:
            queue.pop()
            queue.append((zeros, ones * twos))

        data = data[PIXELS:]
        zeros_queue, product_queue = queue[0]

    return product_queue


if __name__ == "__main__":
    directory: str = os.path.dirname(os.path.abspath(__file__))
    filename: str = os.path.join(directory, "input.txt")
    with open(filename, "r") as fp:
        data: str = fp.read().strip("\n")

    digits: int = get_lowest_digits(data)
    print(f"Answer is: {digits}")
