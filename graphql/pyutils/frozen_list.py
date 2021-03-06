__all__ = ["FrozenList"]

from .frozen_error import FrozenError


class FrozenList(list):
    """List that can only be read, but not changed."""

    def __delitem__(self, key):
        raise FrozenError

    def __setitem__(self, key, value):
        raise FrozenError

    def __add__(self, value):
        if isinstance(value, tuple):
            value = list(value)
        return list.__add__(self, value)

    def __iadd__(self, value):
        raise FrozenError

    def __mul__(self, value):
        return list.__mul__(self, value)

    def __imul__(self, value):
        raise FrozenError

    def append(self, x):
        raise FrozenError

    def extend(self, iterable):
        raise FrozenError

    def insert(self, i, x):
        raise FrozenError

    def remove(self, x):
        raise FrozenError

    def pop(self, i=None):
        raise FrozenError

    def clear(self):
        raise FrozenError

    def sort(self, *, key=None, reverse=False):
        raise FrozenError

    def reverse(self):
        raise FrozenError
