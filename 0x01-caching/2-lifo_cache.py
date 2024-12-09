#!/usr/bin/env python3

"""Task 2: LIFO Caching
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    class to implement LIFO caching
    """

    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        put item into LIFO cache
        """
        if (key is None) or (item is None):
            return
        if len(self.cache_data) + 1 > self.MAX_ITEMS:
            last = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(last))
            self.cache_data.pop(last)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, True)

    def get(self, key):
        """
        get item from LIFO cache
        """
        return self.cache_data.get(key, None)
