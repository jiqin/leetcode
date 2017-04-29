class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        results = set()
        for num in num_count.keys():
            if k == 0:
                if num_count[num] > 1:
                    results.add('{}_{}'.format(num, num))
            else:
                pair_nums = [num - k, num + k]
                for pair_num in pair_nums:
                    if pair_num in num_count:
                        a = min(num, pair_num)
                        b = max(num, pair_num)
                        results.add('{}_{}'.format(a, b))
        return len(results)


from my_algorithm.common_test import run_test_cases

run_test_cases(
    Solution().findPairs,
    (
        ([3, 1, 4, 1, 5], 2, 2),
        ([1, 2, 3, 4, 5], 1, 4),
        ([1, 3, 1, 5, 4], 0, 1),
    ),
)
