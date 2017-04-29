class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]

        0,
        n = 1: 1,
        n = 2: 10, 11,
        n = 4: 100, 101, 110, 111,
        n = 8: 1000, 1001, ...
        r[n + i] = r[i] + 1
        """
        if num <= 0:
            return []
        elif num == 1:
            return [0]

        ret = [None] * num
        ret[0] = 0
        n = 1
        i = 0
        while n + i < num:
            ret[n + i] = ret[i] + 1
            i += 1
            if i == n:
                n *= 2
                i = 0

        return ret

print Solution().countBits(1000)
