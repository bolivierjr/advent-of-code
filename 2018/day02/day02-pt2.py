import os
import sys

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'input.txt')
id_list1 = []
id_list2 = []

with open(filename, 'r') as fp:
    for id_str in fp:
        id_str = id_str.replace('\n', '')
        id_list1.append(id_str)
        id_list2.append(id_str)


def result():
    for id1 in id_list1:
        char_list1 = list(id1)

        for id2 in id_list2[1:]:
            char_list2 = list(id2)
            new_list = []
            match = 0
            num = 0

            for item in char_list2:
                if item == char_list1[num]:
                    match += 1
                    new_list.append(item)

                num += 1

            if len(char_list2) - match == 1:
                return "".join(new_list)


print(f'The result is {result()}.')
