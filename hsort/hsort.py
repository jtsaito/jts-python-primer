import functools

class HSort:
    """Heap sort."""

    def sort(self, array):
        """Sort a list"""
        self._build_heap(array)

        length = len(array) - 1
        return self._build_list(array, length)

    @classmethod
    def _predecessor_index(cls, index):
        if index <= 0:
            return 0
        else:
            return (index - 1) // 2

    @classmethod
    def _left_successor_index(cls, index):
        return (2 * index) + 1

    @classmethod
    def _right_successor_index(cls, index):
        return (2 * index) + 2

    def _build_heap(self, array):
        return self._recursive_heapify(array, 0)

    def _recursive_heapify(self, array, index):
        if index >= len(array): return array

        self._sift_up(array, index)

        return self._recursive_heapify(array, index + 1)

    def _sift_up(self, array, i):
        if i <= 0: return array

        p = self._predecessor_index(i)
        if array[p] < array[i]:
            array[i], array[p] = array[p], array[i]

        self._sift_up(array, i - 1)

    def _build_list(self, array, index):
        if index < 1:
            return array

        if array[0] > array[index]:
            array[0], array[index] = array[index], array[0]
            self._sift_down(array, 0, index-1)

        return self._build_list(array, index-1)

    def _sift_down(self, array, index, end_index):
        if self._left_successor_index(index) >= end_index: return array

        max_index = self._max_index(array, index, end_index)

        if max_index != index:
            array[index], array[max_index] = array[max_index], array[index]
            return self._sift_down(array, max_index, end_index)
        else:
            return array

    def _max_index(self, array, index, end_index):
        left_index = self._left_successor_index(index)
        right_index = self._right_successor_index(index)

        indexes = [index, left_index]
        if right_index <= end_index: indexes.append(right_index)

        def arg_max(a, b): return a if array[a] >= array[b] else b

        return functools.reduce(arg_max, indexes)
