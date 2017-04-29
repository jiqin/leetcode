class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1

        coins.sort()
        return self._inner_coin_change(coins, amount, 0, -1)

    def _inner_coin_change(self, coins, amount, cur_result, global_result):
        """

        :param coins: sorted list of int, e.g. [1, 2, 5]
        :param amount: int, left amount
        :param cur_result:
        :param global_result: max global_result
        :return:
        """
        assert len(coins) > 0

        # if max coin can accumulated into the amount, no need to continue
        if amount % coins[-1] == 0:
            return self._get_result(cur_result + amount / coins[-1], global_result)

        # if only one coin left and it can't mod to 0, return
        if len(coins) == 1:
            return global_result

        max_n = amount / coins[-1]
        for i in range(max_n, -1, -1):  # [max_n, max_n - 1, ... 0]
            if global_result != -1:
                tmp_amount = amount - coins[-1] * i
                tmp_cur_result = cur_result + i
                possible_max_result = tmp_cur_result + tmp_amount / coins[-1]
                if not self._is_valid_cur_result(possible_max_result, global_result):
                    break
            global_result = self._inner_coin_change(coins[0:-1], amount - coins[-1] * i, cur_result + i, global_result)
        return global_result

    def _is_valid_cur_result(self, cur_result, global_result):
        return global_result == -1 or cur_result < global_result

    def _get_result(self, cur_result, global_result):
        return cur_result if self._is_valid_cur_result(cur_result, global_result) else global_result


print Solution().coinChange([1, 2, 5], 11)
print Solution().coinChange([227,99,328,299,42,322], 9847)