class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            v = nums[i]
            while 0 <= v - 1 < len(nums):
                tmp = nums[v - 1]
                nums[v - 1] = v

                if tmp < 1 or tmp > len(nums) or tmp == v:
                    break
                v = tmp
        for i in range(len(nums)):
            v = nums[i]
            if v != i + 1:
                return i + 1
        return len(nums) + 1


def test():
    for nums in (
            [2, 1],
            [4, 1, 2],
            [9, 4, -2, 2, 5, 3, 2, 1, -4, 5],
            [1, 2, 3, 4, 6, 8],
    ):
        print Solution().firstMissingPositive(nums)


test()
