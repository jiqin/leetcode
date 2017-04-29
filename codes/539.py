class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        TOTAL_MINUTE_IN_ONE_DAY = 24 * 60
        times = map(self._str_time_to_int, timePoints)
        times.sort()
        ret = TOTAL_MINUTE_IN_ONE_DAY
        for i in range(1, len(times)):
            ret = min(ret, times[i] - times[i - 1])
        ret = min(ret, self._get_time_diff(times[-1], times[0], TOTAL_MINUTE_IN_ONE_DAY))
        return ret

    def _str_time_to_int(self, s):
        ns = s.split(':')
        return int(ns[0]) * 60 + int(ns[1])

    def _get_time_diff(self, t1, t2, total_minute_in_one_day):
        t = t2 - t1
        if t < 0:
            t += total_minute_in_one_day
        return t


from my_algorithm.common_test import run_test_cases

run_test_cases(
    Solution().findMinDifference,
    (
        (["23:59", "00:00"], 1),
        (["21:59", "00:00"], 121),
        (["23:59", "00:20", "00:01"], 2),
        (["23:59", "00:20", "01:01"], 21),
    ),
)
