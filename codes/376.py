class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        cache = {}
        v1 = self._wiggle(nums, 1, nums[0], True, cache)
        v2 = self._wiggle(nums, 1, nums[0], False, cache)
        return 1 + max(v1, v2)

    def _wiggle(self, nums, start_index, pre_value, flag, cache):
        """

        :param nums: List[int]
        :param start_index: int
        :param pre_value: int, previous value
        :param flag: boolean, the different of current value and previous value, True: positive, False: negative
        :param cache: map[(int, int) => int], (start_index, flag) => result
        :return: int
        """
        assert start_index <= len(nums)
        assert isinstance(flag, bool)
        assert isinstance(cache, dict)
        if start_index == len(nums):
            return 0

        cur_value = nums[start_index]

        if (flag and cur_value > pre_value) or (not flag and cur_value < pre_value):
            key = (start_index, flag)
            if key not in cache:
                value1 = 1 + self._wiggle(nums, start_index + 1, cur_value, not flag, cache)
                value2 = self._wiggle(nums, start_index + 1, pre_value, flag, cache)
                cache[key] = max(value1, value2)
            return cache[key]
        else:
            return self._wiggle(nums, start_index + 1, cur_value, flag, cache)


print Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
print Solution().wiggleMaxLength(range(10))
print Solution().wiggleMaxLength(range(10, 0, -1))
