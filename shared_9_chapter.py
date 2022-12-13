"""
shared utils for chapter 12.
"""

class Item(object):
    """
    simple key-value pair with implemented comparison.
    """

    def __init__(self, key, value, *args, **kwargs):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __repr__(self) -> str:
        return f'Item({self.key}, {self.value})'
