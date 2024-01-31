#!/usr/bin/env python3
"""
LIFO Caching
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
         calls the parent init
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
         assigned to the dictionary self.cache_data the
         item value for the key key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                deleted_key = self.stack.pop()
                del self.cache_data[deleted_key]
                print("DISCARD:", deleted_key)

            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """
        returns the value in self.cache_data linked to key
        """
        if key is not None:
            return self.cache_data.get(key, None)
        return None
