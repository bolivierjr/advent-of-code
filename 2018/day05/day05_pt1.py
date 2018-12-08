import os

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'input.txt')
with open(filename, 'r') as fp:
    data = fp.read()


def reactor(polymers: str) -> str:
    polymers = list(polymers)
    not_found = True

    while not_found:
        reactive_poly = []
        reactive_poly.extend(polymers)
        start = len(reactive_poly)

        for item, _ in enumerate(polymers):
            if item >= len(reactive_poly) - 1:
                break

            elif reactive_poly[item].lower() in reactive_poly[item + 1].lower():
                if reactive_poly is not reactive_poly[item + 1]:
                    reactive_poly.pop(item + 1)
                    reactive_poly.pop(item)

        if len(reactive_poly) == len(polymers):
            not_found = False

        polymers.clear()
        polymers.extend(reactive_poly)

    return ''.join(reactive_poly)


if __name__ == '__main__':
    print(f'Polymer count: {len(reactor(data))}')
