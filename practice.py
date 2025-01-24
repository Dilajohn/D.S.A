# set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
# print("\nSet with the use of mixed values")
# print(set)
# Tuple = ('Geeks', 'for')
# print("\nTuple with the use of strings")
# print(Tuple)

# List1 = [1, 2, 3, 4, 5, 6]
# print("\nTuple using List")
# Tuple = tuple(List1)
# print(Tuple)
# print(Tuple[0])
# print(Tuple[-1])
# print(Tuple[-3])

# print("\nElements of a set")
# for i in set:
    # print(i, end=" ")
# print()
# print("Geeks" in set)


# normal_set = set(["a","b", "c"])

# print("Normal set")
# print(normal_set)

# frozen_set = frozenset(["e", "f", "g"])

# print("\nfrozen set")
# print(frozen_set)

# string = " Welcome to GeeksForGeeks"
# print("Creating string:")
# print(string)

# Dict = {'Name': 'Geeks', 1:[1, 2, 3, 4]}
# print("creating Dictionary: ")
# print(Dict)
# print(Dict['Name'])
# print(Dict.get(1))
# myDict = {x: x**2 for x in [1,2,3,4,5]}
# print(myDict)

import numpy as np

a = np.array([[1,2,3,4],[4,55,1,2],
               [8,3,20,19],[11,2,22,21]])
m = np.reshape(a,(4, 4))
print(m)