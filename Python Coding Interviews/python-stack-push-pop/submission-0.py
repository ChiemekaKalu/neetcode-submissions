from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    revL = []
    while len(arr) != 0:
        revL.append(arr.pop())
    return revL


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
