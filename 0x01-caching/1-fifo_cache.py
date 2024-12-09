#!/usr/bin/env python3

"""Task 1: FIFO caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class for FIFO caching
    """

    def __init__(self):
        """
        constructor
        """
        super().__init__()

    def put(self, key, item):
        """
        add item to FIFO cache
        """
        if (key is not None) and (item is not None):
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            print("DISCARD: {}".format(next(iter(self.cache_data))))
            self.cache_data.pop(next(iter(self.cache_data)))

    def get(self, key):
        """
        get item from FIFO cache
        """
        return self.cache_data.get(key, None)
