# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def find_last_smaller_or_equal(values, v, cmp_func=None):
    """ find last index where values[index] <= v, return None if v < values[0]

    :param values: list
    :param v:
    :param cmp_func: function(a, b) returns -1, 0, 1
    :return: int or None
    """
    if cmp_func is None:
        cmp_func = lambda a, b: -1 if a < b else 0 if a == b else 1

    assert len(values) > 0

    l = 0
    r = len(values)
    while l < r - 1:
        m = (l + r) / 2
        if cmp_func(values[m], v) in (-1, 0):
            l = m
        else:
            r = m

    if cmp_func(values[l], v) == 1:
        return None
    return l


def find_first_bigger_or_equal(values, v, cmp_func=None):
    """ find first index where values[index] >= v, return None if v > values[-1]

    :param values:
    :param v:
    :param cmp_func:
    :return: int or None
    """
    if cmp_func is None:
        cmp_func = lambda a, b: -1 if a < b else 0 if a == b else 1

    assert len(values) > 0

    l = 0
    r = len(values)
    while l < r:
        m = (l + r) / 2
        if cmp_func(values[m], v) == -1:
            l = m + 1
        else:
            r = m

    if l >= len(values):
        return None
    return l


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]

        [x, x], [x, x], [x, x],  [x, x]
                 [x,          x]
        """
        if not intervals:
            return [newInterval]

        cmp_func_s = lambda a, b: -1 if a.start < b.start else 0 if a.start == b.start else 1
        cmp_func_e = lambda a, b: -1 if a.end < b.end else 0 if a.end == b.end else 1
        l = find_last_smaller_or_equal(intervals, newInterval, cmp_func_s)
        r = find_first_bigger_or_equal(intervals, newInterval, cmp_func_e)

        if l is None:
            s = newInterval.start
            l = 0
        elif intervals[l].end < newInterval.start:
            s = newInterval.start
            l += 1
        else:
            s = intervals[l].start

        if r is None:
            e = newInterval.end
            r = len(intervals)
        elif intervals[r].start > newInterval.end:
            e = newInterval.end
        else:
            e = intervals[r].end
            r += 1

        results = intervals[0:l] + [Interval(s, e)] + intervals[r:]
        return results


def test():
    def _to_interval(l):
        return map(lambda v: Interval(v[0], v[1]), l)

    def _to_list(l):
        return map(lambda v: [v.start, v.end], l)

    for i in range(10):
        l = list(range(2, 10, 2))
        print i, find_last_smaller_or_equal(l, i), find_first_bigger_or_equal(l, i), l

    for i, newi in (
            ([], [5, 7]),
            (([1, 3], [4, 6], [7, 10], [11, 15]), [5, 13]),
            (([1, 3], [4, 6], [7, 10], [11, 15]), [0, 1]),
            (([1, 3], [4, 6], [7, 10], [11, 15]), [-1, 0]),
            (([1, 3], [4, 6], [7, 10], [11, 15]), [17, 18]),
            (([1, 3], [6, 9]), [2, 5]),
            (([1, 3], [6, 9]), [2, 7]),
            (([1, 2], [3, 5], [6, 7], [8, 10], [12, 16]), [4, 9]),
    ):
        print _to_list(Solution().insert(_to_interval(i), Interval(newi[0], newi[1])))


test()
