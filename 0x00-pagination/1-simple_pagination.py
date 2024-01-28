#!/usr/bin/env python3
"""
Simple pagination
"""


import csv
import math
from typing import List


def index_range(page, page_size):
    """
    return a tuple of size two containing a start index and an end
    index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Must be positive numbers")
    first_index = (page - 1) * page_size
    last_index = first_index + page_size

    return first_index, last_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns page of dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        first_index, last_index = index_range(page, page_size)
        data = self.dataset()

        if last_index >= len(data):
            return []
        else:
            return data[first_index:last_index]
