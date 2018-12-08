import os
from functools import reduce
from string import ascii_lowercase

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'input.txt')
with open(filename, 'r') as fp:
    data = fp.read()


def reactors2(polymers: str) -> int:
    not_found = True
    polymer_lengths = set()

    while not_found:
        reactive_poly = polymers
        start = len(reactive_poly)

        for x in ascii_lowercase:
            polymers = reactive_poly
            polymers = polymers.replace(
                x.lower(), '').replace(x.upper(), '')

            for item, polymer in enumerate(reactive_poly):
                lowercase_first = polymer.lower() + polymer.upper()
                uppercase_first = polymer.upper() + polymer.lower()
                polymers = polymers.replace(
                    lowercase_first, '').replace(uppercase_first, '')

                if item == len(reactive_poly) - 1:
                    polymer_lengths.add(len(polymers))

            end = len(reactive_poly)
            not_found = start != end

    shortest_length_poly = reduce(
        (lambda x, y: x if x < y else y), polymer_lengths)

    return shortest_length_poly


if __name__ == '__main__':
    print(f'Polymer count: {reactors2(data)}')
