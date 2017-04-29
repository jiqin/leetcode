class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        up_direction = True
        for i in range(0, len(nums) - 1):
            up_direction = not up_direction
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1

            if j == len(nums):
                break

            if (up_direction and nums[i] > nums[j]) or (not up_direction and nums[i] < nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
            else:
                if i + 1 != j:
                    nums[i+1], nums[j] = nums[j], nums[i+1]

        print i, up_direction
        return nums


def valid_result(nums):
    if len(nums) < 2:
        print 'Passed:', nums
        return
    if nums[0] == nums[1]:
        print 'Failed ({} : {}) ({} : {}):'.format(0, 1, nums[0], nums[1]), nums
        return

    up_direction = True if nums[0] < nums[1] else False
    for i in range(0, len(nums) - 1):
        if (up_direction and nums[i] >= nums[i + 1]) or (not up_direction and nums[i] <= nums[i + 1]):
            print 'Failed ({} : {}) ({} : {}):'.format(i, i+1, nums[i], nums[i+1]), nums
            return
        up_direction = not up_direction
    print 'Passed:', nums

valid_result(Solution().wiggleSort([1, 2, 3, 4, 5, 6]))
valid_result(Solution().wiggleSort([1, 5, 2, 3, 1, 1, 1, 2, 1, 1, 4]))
valid_result(Solution().wiggleSort([2, 1, 5, 2, 1, 1, 1]))
valid_result(Solution().wiggleSort([2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

# 2 4 3 6 5 8 7 9 1  1 1 1 1 1 1
