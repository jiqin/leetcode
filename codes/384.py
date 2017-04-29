import copy
import random


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self._original_nums = copy.copy(nums)
        self._nums = copy.copy(nums)
        self._rand = random.Random()

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self._original_nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self._nums) - 1):
            n = self._rand.randint(i, len(self._nums) - 1)
            self._nums[i], self._nums[n] = self._nums[n], self._nums[i]
        return self._nums


# Your Solution object will be instantiated and called as such:
obj = Solution(list(range(10)))
print obj.reset()
for i in range(10):
    print obj.shuffle()
