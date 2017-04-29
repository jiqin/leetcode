class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        nums.sort()
        results = [[0, None] for _ in range(len(nums))]  # [[length of tail, last index], ...]
        for i in range(1, len(nums)):
            tmp_value = [0, None]
            for j in range(0, i):
                if nums[i] % nums[j] != 0:
                    continue
                if tmp_value[0] == 0:
                    tmp_value = [1, j]
                elif (results[j][0] + 1) > tmp_value[0]:
                    tmp_value = [results[j][0] + 1, j]
            results[i] = tmp_value

        max_index = 0
        for i in range(0, len(results)):
            if results[i][0] > results[max_index][0]:
                max_index = i
        result = []
        while max_index is not None:
            result.insert(0, nums[max_index])
            max_index = results[max_index][1]
        return result


# print Solution().largestDivisibleSubset(range(1,100))
# print Solution().largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824])
# print Solution().largestDivisibleSubset([pow(2, i) for i in range(31)])
# print Solution().largestDivisibleSubset([pow(2, i) for i in range(30)])
# print Solution().largestDivisibleSubset([3, 4, 16, 8])


# 367

def solution(num):
    m = 2
    n = num
    while m * m <= n:
        if n % m != 0:
            m += 1
            continue

        n /= m
        if n % m != 0:
            return False
        n /= m
    return n == 1


from math import sqrt
for i in range(10000000):
    if solution(i):
        print i, sqrt(i)
