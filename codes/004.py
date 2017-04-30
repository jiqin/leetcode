class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total_count = len(nums1) + len(nums2)
        if total_count == 0:
            return 0

        mid_count = int(total_count / 2)
        odd = total_count % 2

        l, r = 0, len(nums1)
        while l <= r:
            i = int((l + r) / 2)
            j = mid_count - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                r = i - 1
            elif i < len(nums1) and nums1[i] < nums2[j - 1]:
                l = i + 1
            else:
                break

        if odd:
            if i == len(nums1):
                return nums2[j]
            else:
                return min(nums1[i], nums2[j])
        else:

            if i == 0:
                lv = nums2[j - 1]
            elif j == 0:
                lv = nums1[i - 1]
            else:
                lv = max(nums1[i - 1], nums2[j - 1])

            if i == len(nums1):
                rv = nums2[j]
            elif j == len(nums2):
                rv = nums1[i]
            else:
                rv = min(nums1[i], nums2[j])

            return (lv + rv) / 2.0


from tools.common_test import run_test_cases


run_test_cases(
    Solution().findMedianSortedArrays,
    (
        (
            [1, 2],
            [3, 4],
            2.5,
        ),
        (
            [],
            [2, 3],
            2.5,
        ),
        (
            [1],
            [2, 3],
            2,
        ),
        (
            [1, 2, 3, 4],
            [2, 3],
            2.5,
        ),
        (
            [1, 9],
            [2, 3, 4],
            3,
        ),
    ),
)
