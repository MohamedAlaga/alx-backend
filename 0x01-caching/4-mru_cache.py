#!/usr/bin/env python3

"""Task 3: MRU Caching
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    class to implement MRUCache caching
    """

    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        put item into MRUCache cache
        """
        if (key is not None) and (item is not None):
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) + 1 > self.MAX_ITEMS:
                    last = list(self.cache_data.keys())[-1]
                    print("DISCARD: {}".format(last))
                    self.cache_data.pop(last)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, True)

    def get(self, key):
        """
        get item from MRUCache cache
        """
        if (key is not None) and (key in self.cache_data):
            self.cache_data.move_to_end(key, True)
        return self.cache_data.get(key, None)
