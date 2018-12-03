import os

directory: str = os.path.dirname(os.path.abspath(__file__))
filename: str = os.path.join(directory, 'input.txt')


with open(filename, 'r') as fp:
    for id_str in fp:
        pass

print(f'')
