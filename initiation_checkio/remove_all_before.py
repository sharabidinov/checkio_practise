# Remove from the list all of the elements before the given one.
from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    for i in range(0, len(items)):
        if items[i] == border:
            return items[i:]

    return items


if __name__ == '__main__':
    print(remove_all_before([1, 2, 3, 4, 5], 3))
    print(remove_all_before([1, 1, 2, 2, 3, 3], 2))
    print(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2))
    print(remove_all_before([1, 1, 5, 6, 7], 2))
    print(remove_all_before([], 0))
    print(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7))
