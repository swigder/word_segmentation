from utilities.utilities import binary_search
from collections import namedtuple


Item = namedtuple('Item', ['key', 'value'])


class SpaceEfficientDict:
    """
    Python dicts have a lot of space overhead. This dict is optimized for space at the cost of some additional time.
    Note: Class is subscriptable for reading, but for writing "set" must be used.
    """
    data = []

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        index = self.__key_index(item)
        return self.data[index].value if index >= 0 else None

    def __key_index(self, lookup_key, insert=False):
        return binary_search(self.data, lookup_key, lambda k, item: 0 if k == item.key else 1 if k > item.key else -1,
                             insertion_index=insert)

    def set(self, key, value):
        """
        Set the key to value, or insert key with value if key is not yet present.
        Runs in O(log n) if key is present, otherwise O(n).
        :param key: key to insert
        :param value: value to insert
        """
        index, insertion_index = self.__key_index(lookup_key=key, insert=True)
        if index >= 0:
            self.data[index] = Item(key=key, value=value)
        else:
            self.data.insert(insertion_index, Item(key=key, value=value))

    def increment(self, key):
        """
        Increments the value of key, or inserts key with value 1 if key is not yet present.
        Runs in O(log n) if key is present, otherwise O(n).
        :param key: key to increment
        """
        index, insertion_index = self.__key_index(lookup_key=key, insert=True)
        if index >= 0:
            self.data[index] = Item(key=key, value=self.data[index].value + 1)
        else:
            self.data.insert(insertion_index, Item(key=key, value=1))

    def get(self, key):
        """
        Get the value for a given key. Runs in O(log n).
        :param key: key to look up
        :return: the value for the given key if key is in the dict, None otherwise
        """
        index = self.__key_index(lookup_key=key)
        return self.data[index].value if index >= 0 else None
