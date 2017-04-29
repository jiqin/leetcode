class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(i, 0, matrix[i][0]) for i in range(len(matrix))]
        for _ in range(k):
            value = self.next_value(matrix, heap)
        return value

    def next_value(self, matrix, heap):
        """

        :param matrix:
        :param heap: [(row index, col index, value), ...]
        :return: value
        """
        row_index, col_index, value = heap[0]
        col_index += 1
        if col_index == len(matrix[0]):
            head = heap.pop(-1)
        else:
            head = (row_index, col_index, matrix[row_index][col_index])
        if heap:
            heap[0] = head

        parent = 0
        while True:
            next_index = parent
            l_child = parent * 2 + 1
            r_child = l_child + 1
            if l_child < len(heap):
                if heap[next_index][2] > heap[l_child][2]:
                    next_index = l_child
            if r_child < len(heap):
                if heap[next_index][2] > heap[r_child][2]:
                    next_index = r_child
            if next_index != parent:
                heap[parent], heap[next_index] = heap[next_index], heap[parent]
                parent = next_index
            else:
                break

        return value


m1 = [
    [1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8],
    [4, 5, 6, 7, 8, 9],
    [5, 6, 7, 8, 9, 10],
    [6, 7, 8, 9, 10, 11],
]
v1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 11]

for i, v in enumerate(v1):
    assert Solution().kthSmallest(m1, i+1) == v, '{} {}'.format(i, v)

m1 = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]
v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

for i, v in enumerate(v1):
    assert Solution().kthSmallest(m1, i+1) == v, '{} {}'.format(i, v)
