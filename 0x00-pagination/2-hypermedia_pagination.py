#!/usr/bin/env python3
"""
Hypermedia pagination
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        returns a dictionary containing the following key-value pairs:

        -page_size: the length of the returned dataset page
        -page: the current page number
        -data: the dataset page (equivalent to return from previous task)
        -next_page: number of the next page, None if no next page
        -prev_page: number of the previous page, None if no previous page
        -total_pages: the total number of pages in the dataset as an integer
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        current_page = page
        data_page = self.get_page(page, page_size)
        nextPage = current_page + 1 if len(data_page) == page_size else None
        prevPage = current_page - 1 if current_page > 1 else None
        total_pages = math.ceil(len(self.dataset()) / page_size)

        info = {
            "page_size": len(data_page),
            "page": current_page,
            "data": data_page,
            "next_page": nextPage,
            "prev_page": prevPage,
            "total_pages": total_pages
        }

        return info
