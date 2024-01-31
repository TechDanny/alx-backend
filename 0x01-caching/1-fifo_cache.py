#!/usr/bin/env python3
"""
FIFO caching
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
         calls the parent init
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the
        item value for the key key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                deleted_key = self.queue.pop(0)
                del self.cache_data[deleted_key]
                print("DISCARD:", deleted_key)

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        returns the value in self.cache_data linked to key
        """
        if key is not None:
            return self.cache_data.get(key, None)
        return None
