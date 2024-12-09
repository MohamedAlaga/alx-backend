#!/usr/bin/env python3

"""Task 3: LRU Caching
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    class to implement LRUCache caching
    """

    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        put item into LRUCache cache
        """
        if (key is not None) and (item is not None):
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) + 1 > self.MAX_ITEMS:
                    first = next(iter(self.cache_data))
                    print("DISCARD: {}".format(first))
                    self.cache_data.pop(first)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, True)

    def get(self, key):
        """
        get item from LRUCache cache
        """
        if (key is not None) and (key in self.cache_data):
            self.cache_data.move_to_end(key, True)
        return self.cache_data.get(key, None)
