class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        return self._process(boxes, {})

    def _find_next_value_range(self, boxes, index, value):
        left = index
        while left < len(boxes) and boxes[left] != value:
            left += 1

        right = left + 1
        while right < len(boxes) and boxes[right] == value:
            right += 1

        return left, right

    def _process(self, boxes, cached):
        if len(boxes) == 0:
            return 0
        elif len(boxes) == 1:
            return 1

        key = '_'.join(map(str, boxes))
        r = cached.get(key)
        if r is not None:
            return r

        start0, end0 = self._find_next_value_range(boxes, 0, boxes[0])
        r = (end0 - start0) * (end0 - start0) + self._process(boxes[end0:], cached)

        start1 = end0
        while True:
            start1, end1 = self._find_next_value_range(boxes, start1, boxes[0])
            if start1 >= len(boxes):
                break

            r1 = self._process(boxes[end0:start1], cached) + self._process(boxes[0:end0] + boxes[start1:], cached)
            r = max(r, r1)

            start1 = end1

        cached[key] = r
        return r


from my_algorithm.common_test import run_test_cases

run_test_cases(
    Solution().removeBoxes,
    (
        ([1, 1], 4),
        ([1, 3, 2, 2, 2, 3, 4, 3, 1], 23),
        ([1, 2, 1, 2, 1, 2, 1, 2, 1], 29),
        (
        [3, 8, 8, 5, 5, 3, 9, 2, 4, 4, 6, 5, 8, 4, 8, 6, 9, 6, 2, 8, 6, 4, 1, 9, 5, 3, 10, 5, 3, 3, 9, 8, 8, 6, 5, 3, 7,
         4, 9, 6, 3, 9, 4, 3, 5, 10, 7, 6, 10, 7], 136),
    ),
)
