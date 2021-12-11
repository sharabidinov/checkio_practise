# In a given list the first element should become the last one. An empty list or list with only one element should stay
# the same.
from typing import Iterable


def replace_first(items: list) -> Iterable:
    return items[1:len(items):] + items[0:1:]
