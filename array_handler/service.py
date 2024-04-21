class ArrayHandler:
    def __init__(self, array: list[int]):
        self._array = array
        self._first_element = self._array[0]

    def max_element(self):
        return max(self._array)

    def min_element(self):
        return min(self._array)

    def swap_max_and_first(self):
        max_element = self.max_element()
        max_index = self._find_index(max_element)
        result = self._array.copy()
        result[0], result[max_index] = result[max_index], result[0]
        return result

    @property
    def get_array(self):
        return self._array

    def sum_between_min_and_max(self):
        min_element_index = self._find_index(self.min_element())
        max_element_index = self._find_index(self.max_element())
        borders = self._start_and_end_indexes(min_element_index, max_element_index)
        cut_array = self._array[borders["start"]:borders["end"]+1]
        return sum(cut_array)

    def write_sum_min_to_max_in_last(self):
        result = self._array.copy()
        result[-1] = self.sum_between_min_and_max()
        return result

    def _start_and_end_indexes(self, first_index, second_index):
        if first_index < second_index:
            return {"start": first_index, "end": second_index}
        return {"start": second_index, "end": first_index}

    def _find_index(self, element):
        return self._array.index(element)
