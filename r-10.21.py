"""
Consider the following variant of the _find_index method from Code Fragment 10.8 in the context of
the SortedTableMap class:

    def _find_index(self, key, low, high):
        if high < low:
            return high + 1
        else:
            mid = (high + low) // 2
            if self.table[mid].key < key:
                return self._find_index(key, mid + 1, high)
            else:
                return self._find_index(key, low, mid - 1)

"""


class SortedTableMap():
    """
    partial implementation of the SortedTableMap
    """

    def __init__(self, *args, **kwargs):
        self.table = []

    class Item(object):

        def __init__(self, key, value):
            self.key = key
            self.value = value

    def _find_index(self, key, low, high):
        """
        original find index method
        """
        if high < low:
            return high + 1
        else:
            mid = (high + low) // 2
            if self.table[mid].key == key:
                return mid
            elif self.table[mid].key < key:
                return self._find_index(key, mid + 1, high)
            else:
                return self._find_index(key, low, mid - 1)

    def _find_index_2(self, key, low, high):
        """
        modified method
        """
        if high < low:
            return high + 1
        else:
            mid = (high + low) // 2
            # if self.table[mid].key == key:
            #     return mid
            if self.table[mid].key < key:
                return self._find_index_2(key, mid + 1, high)
            else:
                return self._find_index_2(key, low, mid - 1)


if __name__ == "__main__":

    map = SortedTableMap()

    vals = [5, 6, 7, 8, 11, 13, 15, 19, 21, 23]

    for i in range(0, len(vals)):
        map.table.append(SortedTableMap.Item(vals[i], str(vals[i])))

    for val in vals:
        assert map._find_index(val, 0, len(map.table)-1) == map._find_index_2(val, 0, len(map.table)-1)

    # answer yes it does, you can even return low when high < low, but high + 1 makes more sense,
    # if given key is not in the list, that will be the next available position
