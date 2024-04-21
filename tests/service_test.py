from array_handler.service import ArrayHandler


class TestArrayHandler:
    def setup_method(self):
        self.test_data = list(range(-10, 11))
        self.array_handler = ArrayHandler(array=self.test_data)

    def test_max_element(self):
        assert self.array_handler.max_element() == 10

    def test_min_element(self):
        assert self.array_handler.min_element() == -10

    def test_swap_first_and_max(self):
        assert self.array_handler.swap_max_and_first() == [10, -9, -8, -7,-6, -5, -4, -3, -2,
                                                           -1, 0, 1, 2, 3, 4, 5,6, 7, 8, 9, -10]
        assert self.array_handler.get_array == self.test_data

    def test_sum_between_min_and_max(self):
        assert self.array_handler.sum_between_min_and_max() == 0
        assert self.array_handler.get_array == self.test_data

    def test_write_sum_min_to_max_in_last(self):
        assert self.array_handler.write_sum_min_to_max_in_last() == [-10, -9, -8, -7, -6, -5, -4, -3, -2,
                                                           -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


class TestArrayHandlerOneElement:
    def setup_method(self):
        self.test_data = [5]
        self.array_handler = ArrayHandler(array=self.test_data)

    def test_max_element(self):
        assert self.array_handler.max_element() == 5

    def test_min_element(self):
        assert self.array_handler.min_element() == 5

    def test_swap_first_and_max(self):
        assert self.array_handler.swap_max_and_first() == [5]
        assert self.array_handler.get_array == self.test_data

    def test_sum_between_min_and_max(self):
        assert self.array_handler.sum_between_min_and_max() == 5
        assert self.array_handler.get_array == self.test_data

    def test_write_sum_min_to_max_in_last(self):
        assert self.array_handler.write_sum_min_to_max_in_last() == [5]
