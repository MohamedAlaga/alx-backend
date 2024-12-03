#!/usr/bin/env python3
"""
module contains index_range function
"""


def index_range(page, page_size) -> tuple:
    start_index = page * page_size
    end_index = start_index + page_size
    return start_index, end_index
