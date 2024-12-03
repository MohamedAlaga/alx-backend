#!/usr/bin/env python3
"""
module contains index_range function
"""


def index_range(page, page_size) -> tuple:
    """
    :param page: page number
    :param page_size: the size of the page
    :return: tuple containing start and end index
    """
    start_index = (page-1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)