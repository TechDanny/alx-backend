#!/usr/bin/env python3
"""
LRU Caching
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
     inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        calls the parent init
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        assigned to the dictionary self.cache_data
        the item value for the key key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                leastRecently_key = self.order.pop(0)
                del self.cache_data[leastRecently_key]
                print("DISCARD:", leastRecently_key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        returns the value in self.cache_data linked to key
        """
        if key is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None
