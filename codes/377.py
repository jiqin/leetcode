from copy import copy


class Factorial(object):
    def __init__(self):
        self._cache = [None] * 1000
        self._cache[0] = 1
        self._size = 1

    def fn(self, n):
        """ return n! = n * (n-1) * ... * 2 * 1

        :param n: int
        :return: int
        """
        if n <= 0:
            return 1

        if len(self._cache) <= n:
            tmp_cache = [None] * (n * 2)
            for i in range(len(self._cache)):
                tmp_cache[i] = self._cache[i]
            self._cache = tmp_cache
        if self._size < n + 1:
            for i in range(self._size, n+1):
                self._cache[i] = i * self._cache[i-1]
            self._size = n + 1
        return self._cache[n]

    def ffn(self, nums):
        """ return (n1 + n2 + ... nm)! / (n1! * n2! * ... * nm!)

        :param nums: List(int)
        :return: int
        """
        result = self.fn(sum(nums))
        for num in nums:
            result /= self.fn(num)
        return result


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        factorial = Factorial()

        nums.sort()

        result_cache = {}
        self._combination(nums, 0, target, result_cache)
        result = result_cache.get((0, target))
        print sum(map(factorial.ffn, result))
        result_cache = {}
        result = self._combination2(nums, target, result_cache)
        print result
        return None

    def _combination2(self, nums, target, result_cache):
        """

        :param nums: list[int]
        :param target: int
        :param result_cache: map: int => int, target: result
        :return: int
        """
        assert target > 0
        if target in result_cache:
            return result_cache[target]

        result = 0
        for n in nums:
            tmp_target = target - n
            if tmp_target == 0:
                result += 1
            elif tmp_target > 0:
                result += self._combination2(nums, tmp_target, result_cache)
        result_cache[target] = result
        return result

    def _combination(self, nums, start_index, target, result_cache):
        """

        :param nums: list[int]
        :param target: int, target value
        :param result_cache: map((start_index, target) => list[list[int]])
                e.g.
                {
                    (1, 1) : [],
                    (1, 2) : [[1, 0, 0, 0], [2, 0, 0, 0]],
                }
        :return: list[list[int]]
        """
        assert start_index < len(nums)
        assert target >= 0

        key = (start_index, target)
        result = result_cache.get(key)
        if result is not None:
            return result

        result = []
        if target == 0:
            result.append([])
        else:
            value = target / nums[start_index]
            if start_index == len(nums) - 1:
                if target % nums[start_index] == 0:
                    result.append([value])
            else:
                for cur_count in range(0, value + 1):
                    tmp_result = self._combination(nums, start_index + 1, target - nums[start_index] * cur_count, result_cache)
                    if cur_count == 0:
                        result.extend(tmp_result)
                    else:
                        result.extend(map(lambda l: [cur_count] + l, tmp_result))
        result_cache[key] = result
        return result


print Solution().combinationSum4([1,2,3], 7)
print Solution().combinationSum4([3,33,333], 1000)
print Solution().combinationSum4(
    [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,930,940,950,960,970,980,990,111],
    999)
