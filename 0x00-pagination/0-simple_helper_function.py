#!/usr/bin/env python3
"""
Simple helper function
"""


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
