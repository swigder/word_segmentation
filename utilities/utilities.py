def binary_search(items, item, comparator=(lambda x, y: 0 if x == y else 1 if x > y else -1), lo=0, hi=None,
                  insertion_index=False):
    """
    Does a binary search on a list using a custom comparator
    :param items: sorted list of items to search
    :param item: item to find
    :param comparator: fn(x, y) => 0 if x == y, 1 if x > y, -1 if x < y, will used built in ==, >, < if not provided
    :param lo: lower boundary to search, start of list if not provided
    :param hi: upper boundary to search, end of list if not provided
    :param insertion_index if set, will return the insertion index for item
    :return: index of item if found, -1 otherwise; if insertion_location is set, will return tuple where second item is
    index of first element in items that is larger than item
    """
    if hi is None:
        hi = len(items)

    while lo < hi:
        mid = (lo+hi) // 2
        comparison = comparator(item, items[mid])
        if comparison == 0:
            return mid if not insertion_index else (mid, mid)
        elif comparison == 1:
            lo = mid+1
        else:
            hi = mid

    return -1 if not insertion_index else (-1, lo)


def bisect_string(string, location):
    return string[:location], string[location:]
