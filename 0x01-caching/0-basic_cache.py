#!/usr/bin/env python3
""" BaseCaching module
"""


class BaseCaching:
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")


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
