class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > 2 * nums[j]:
                    ret += 1
        return ret


from my_algorithm.common_test import run_test_cases

run_test_cases(
    Solution().reversePairs,
    (
        ([1, 3, 2, 3, 1], 2),
        ([2, 4, 3, 5, 1], 3),
        (list(range(1000)), 0),
        (list(range(2000)), 0),
        (list(range(5000)), 0),
    ),
    print_time=True,
)
