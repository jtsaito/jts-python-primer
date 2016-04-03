import functools

class HSort:

    def sort(self, list):
      self._build_heap(list)

      length = len(list) - 1
      return self._build_list(list, length)

    def _build_heap(self, list):
       return self._recursive_heapify(list, 0)

    def _recursive_heapify(self, list, index):
        if index >= len(list): return list

        self._sift_up(list, index)

        return self._recursive_heapify(list, index + 1)

    def _sift_up(self, list, i):
        if i <= 0: return list

        p = self._predecessor_index(i)
        if list[p] < list[i]:
            list[i], list[p] = list[p], list[i]

        self._sift_up(list, i - 1)

    def _predecessor_index(self, index):
        return 0 if index <= 0 else (index - 1) // 2

    def _left_successor_index(self, index):
        return (2 * index) + 1

    def _right_successor_index(self, index):
        return (2 * index) + 2

    def _build_list(self, list, index):
        if index < 1: return list

        if list[0] > list[index]:
            list[0], list[index] = list[index], list[0]
            self._sift_down(list, 0, index-1)

        return self._build_list(list, index-1)

    def _sift_down(self, list, index, end_index):
        if self._left_successor_index(index) >= end_index: return list

        max_index = self._max_index(list, index, end_index)

        if max_index != index:
            list[index], list[max_index] = list[max_index], list[index]
            return self._sift_down(list, max_index, end_index)
        else:
            return list

    def _max_index(self, list, index, end_index):
        left_index = self._left_successor_index(index)
        right_index = self._right_successor_index(index)

        indexes = [index, left_index]
        if right_index <= end_index: indexes.append(right_index)

        arg_max = lambda a, b: a if list[a] >= list[b] else b

        return functools.reduce(arg_max, indexes)
