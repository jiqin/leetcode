class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # import pdb; pdb.set_trace()
        pow_2_list = self._get_pow_2_list(n)
        max_pow_2_index = len(pow_2_list)
        if pow_2_list[-1] != n:
            max_pow_2_index -= 1

        nums = self._convert_nums(nums)

        v = 0
        for i in range(max_pow_2_index):
            if not self._can_sum_up_to_value(nums, pow_2_list[i]):
                v += 1
        return v

    def _get_pow_2_list(self, n):
        pow_2_list = [1]
        while pow_2_list[-1] < n:
            v = pow_2_list[-1]
            v *= 2
            pow_2_list.append(v)
        return pow_2_list

    def _convert_nums(self, nums):
        d = {}
        for v in nums:
            d[v] = d.get(v, 0) + 1
        return d

    def _can_sum_up_to_value(self, nums, v):
        return False

    def assert_value(self, nums, n, c):
        v = Solution().minPatches(nums, n)
        print '{}: {} : {} ==== {} : {}'.format('Passed' if v == c else 'Failed', v, c, n, nums)

Solution().assert_value([], 7, 3)
Solution().assert_value([1, 3], 6, 1)
Solution().assert_value([1, 2, 2], 5, 0)
Solution().assert_value([1, 5, 10], 20, 2)
Solution().assert_value([1,2,31,33], 2147483647, 100)
Solution().assert_value([1,1,1,2,2,2,2,2,3,3,3,4,4,4,5,5,6,6,7,8,8,9,9,9,10,10,11,11,11,11,11,11,11,11,12,12,12,12,12,13,13,14,14,15,15,15,17,19,19,19,19,20,20,20,20,21,21,21,21,21,21,21,22,23,23,23,23,23,24,24,24,25,25,26,26,26,26,27,27,28,28,28,28,29,30,30,31,31,31,31,32,32,33,33,33,34,34,35,35,35,36,36,36,36,36,37,37,37,38,38,38,38,38,38,39,39,39,41,41,41,41,42,42,42,43,43,43,43,43,44,44,44,46,46,46,47,47,47,48,50,50,50,50,51,51,51,51,51,52,52,52,52,52,52,52,52,53,53,54,54,55,56,56,57,57,57,57,57,57,58,58,59,59,59,60,60,60,60,62,62,62,62,63,63,63,63,63,64,64,64,64,64,64,65,65,65,65,65,65,65,66,66,66,66,67,67,67,67,67,68,68,68,69,69,69,69,69,70,70,71,71,72,72,72,72,72,74,74,74,74,75,75,75,75,76,76,76,76,77,78,79,79,79,79,79,80,81,81,82,83,84,84,84,84,84,85,86,86,86,87,87,87,87,88,88,88,89,90,90,90,90,90,91,91,91,91,92,92,93,93,93,94,94,94,95,95,95,95,96,96,97,97,97,97,98,99,99,99,99,100], 3559, 100)
Solution().assert_value([4,6,10,20,25,42,46,50,52,60,64,67,69,80,83,102,109,111,112,112,117,119,120,123,131,132,134,134,136,138,138,139,141,145,146,151,151,167,175,178,183,186,189,194,198,200,205,205,212,222,235,236,247,255,256,262,267,271,278,283,296,296,297,300,307,320,321,322,327,332,365,371,376,380,380,388,393,393,403,413,415,415,422,423,426,436,442,443,445,456,460,462,463,464,464,464,470,477,478,491,491,494,496,512,515,516,518,524,527,533,535,538,539,550,552,555,567,574,580,580,580,581,584,587,587,589,591,598,603,604,605,609,612,612,616,621,624,625,626,638,641,641,644,649,649,649,656,659,665,682,685,699,703,708,717,717,720,728,745,749,768,771,772,780,784,785,786,789,803,807,832,837,841,849,870,886,892,897,904,904,906,911,913,915,916,917,918,922,924,930,938,939,941,942,942,945,948,953,984,1000], 873081, 100)