import os

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'input.txt')
with open(filename, 'r') as fp:
    data = fp.read()


def reactors(polymers: str) -> str:
    not_found = True

    while not_found:
        reactive_poly = polymers
        start = len(polymers)

        for item, polymer in enumerate(reactive_poly):
            lowercase_first = polymer.lower() + polymer.upper()
            uppercase_first = polymer.upper() + polymer.lower()
            polymers = polymers.replace(
                lowercase_first, '').replace(uppercase_first, '')

            end = len(polymers)
            not_found = start != end

    return polymers


if __name__ == '__main__':
    tdata = 'dabAcCaCBAcCcaDA'
    print(f'Polymer count: {len(reactors(data))}')
