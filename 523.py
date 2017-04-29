class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        if k == 0:
            for i in range(0, len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            if nums[i] % k == 0:
                return True

        for i in range(0, len(nums)):
            for j in range(i + 2, len(nums)):
                if (nums[j] - nums[i]) % k == 0:
                    return True
        return False


def test():
    for nums, k, exp_ret in (
        ([23, 2, 4, 6, 7], 0, False),
        ([23, 0, 0, 6, 7], 0, True),
        ([23, 2, 4, 6, 7], 6, True),
        ([23, 2, 6, 4, 7], 6, True),
        ([23, 4, 6, 4, 7], 6, False),
    ):
        ret = Solution().checkSubarraySum(nums, k)
        if ret == exp_ret:
            print 'passed'
        else:
            print nums
            print k
            print ret
            print '>' * 10, 'Failed'


test()
