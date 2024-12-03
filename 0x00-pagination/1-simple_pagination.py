#!/usr/bin/env python3
"""
module contains index_range , function
"""

import csv
from typing import List


def index_range(page, page_size) -> tuple:
    """
    :param page: page number
    :param page_size: the size of the page
    :return: tuple containing start and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
        :param page: page number
        :param page_size: size of the page
        :return: list of page data
        """
        dataset = Server().dataset()
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)
        page_range = index_range(page, page_size)
        if page_range[0] > len(dataset):
            return []
        return dataset[page_range[0]: page_range[1]]
