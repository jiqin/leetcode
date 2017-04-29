class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = [[None] * n for _ in range(n)]
        r = self._getMoneyAmount(cache, 1, n)
        print cache
        return r

    def _getMoneyAmount(self, cache, start_num, end_num):
        """
        : [start_num, end_num]
        """

        if start_num > end_num:
            return 0

        if cache[start_num-1][end_num-1] is not None:
            return cache[start_num-1][end_num-1]

        diff = end_num - start_num
        if diff == 0:  # e.g. [1]
            result = 0
        elif diff == 1:  # e.g. [1,2], first guess 1
            result = start_num
        elif diff == 2:  # e.g. [1,2,3], first guess 2
            result = start_num + 1
        else:
            tmp_results = []
            for i in range(start_num, end_num + 1):
                tmp_results.append(i + max(self._getMoneyAmount(cache, start_num, i - 1),
                                           self._getMoneyAmount(cache, i + 1, end_num)))
            print start_num, end_num, tmp_results
            result = min(tmp_results)

        cache[start_num-1][end_num-1] = result
        print start_num, end_num, result
        return result


print Solution().getMoneyAmount(10)
