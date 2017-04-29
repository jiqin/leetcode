class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self._jump3(nums)

    def _jump3(self, nums):
        results = [len(nums)] * len(nums)
        queue = [(0, 1, nums[0])]
        results[0] = 0

        # print nums
        while queue:
            index, min_step, max_step = queue.pop(0)
            cur_result = results[index] + 1

            for i in range(min_step, max_step + 1):
                next_index = index + i
                if next_index >= len(results):
                    break

                if cur_result < results[next_index]:
                    results[next_index] = cur_result

                    next_min_step = max_step - i + 1
                    next_max_step = nums[next_index]

                    if next_max_step >= next_min_step:
                        queue.append((next_index, next_min_step, next_max_step))

            # print queue
            # print results

        return results[-1]

    def _jump2(self, nums):
        index_set = set([0])
        step = 0
        while (len(nums) - 1) not in index_set:
            step += 1

            tmp_set = set()
            for i in index_set:
                for j in range(1, nums[i] + 1):
                    v = i + j
                    if v not in index_set:
                        tmp_set.add(v)
                    if v == len(nums) - 1:
                        break
                if (len(nums) - 1) in tmp_set:
                    break
            print step, tmp_set, index_set
            index_set = tmp_set
        return step

    def _jump1(self, nums, index=0, cached={}):
        r = cached.get(index)
        if r is not None:
            return r

        if index >= len(nums) - 1:
            return 0

        if nums[index] == 0:
            r = len(nums)
        else:
            rs = []
            for i in range(1, nums[index] + 1):
                rs.append(1 + self._jump1(nums, index + i, cached))

            r = min(rs)
        cached[index] = r
        return r


def test():
    for nums in (
            [5, 8, 1, 8, 9, 8, 7, 1, 7, 5, 8, 6, 5, 4, 7, 3, 9, 9, 0, 6, 6, 3, 4, 8, 0, 5, 8, 9, 5, 3, 7, 2, 1, 8, 2, 3,
             8, 9, 4, 7, 6, 2, 5, 2, 8, 2, 7, 9, 3, 7, 6, 9, 2, 0, 8, 2, 7, 8, 4, 4, 1, 1, 6, 4, 1, 0, 7, 2, 0, 3, 9, 8,
             7, 7, 0, 6, 9, 9, 7, 3, 6, 3, 4, 8, 6, 4, 3, 3, 2, 7, 8, 5, 8, 6, 0],
            list(range(10, 0, -1)) + [1, 0],
            [9, 8, 2, 2, 0, 2, 2, 0, 4, 1, 5, 7, 9, 6, 6, 0, 6, 5, 0, 5],
            [2, 3, 1, 1, 4],
            [1] * 100,
            [1] * 10000,
            list(range(250, 0, -1)) + [1, 0],
            list(range(25000, 0, -1)) + [1, 0],
    ):
        print Solution().jump(nums)


test()
