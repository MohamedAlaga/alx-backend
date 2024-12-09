#!/usr/bin/env python3
"""
basic cashing module
"""
BaseCaching = __import__('base_caching').BasicCache


class BasicCache(BaseCaching):
    """
    class for basic caching with no limits
    """

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if (item is not None) or (key is None):
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
