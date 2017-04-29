class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n2 = [a for a in nums]
        n2.sort()
        n3 = [n2[i+1] - n2[i] for i in range(0, len(n2) - 1)]
        return max(n3)


def test():
    for nums, er in (
            ([1, 2, 4, 8, 16], 8),
            ([1, 20, 4, 8, 16], 8),
            ([1, 40, 4, 8, 16], 24),
            ([1, 40, 4, 8, 16, 4, 5], 24),
            ([10, 40, 4, 8, 16, 4, 5], 24),
            ([10, 20, 4, 8, 16, 4, 5], 6),
    ):
        ar = Solution().maximumGap(nums)
        if er == ar:
            print 'Passed:', nums, er
        else:
            print '>>>>> Failed:', nums, er, ar


test()
