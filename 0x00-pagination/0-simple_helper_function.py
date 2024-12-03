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
