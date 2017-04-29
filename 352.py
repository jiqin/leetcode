# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

from collections import defaultdict

d = defaultdict(lambda: 0)
d[1] += 1
d[1] += 1
d[1] += 1
print d

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []


    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if not self.intervals:
            self.intervals.append(Interval(val, val))

        index = self.findIndex(val)
        if index < 0:
            if val + 1 == self.intervals[0].start:
                self.intervals[0].start = val
            else:
                self.intervals.insert(0, Interval(val, val))
        elif val <= self.intervals[index].end:
            pass
        elif val == self.intervals[index].end + 1:
            if index + 1 == len(self.intervals) or val + 1 < self.intervals[index+1].start:
                self.intervals[index].end = val
            else:
                self.intervals[index].end = self.intervals[index+1].end
                self.intervals = self.intervals[0:index+1] + self.intervals[index+2:]
        elif index + 1 < len(self.intervals) and val + 1 == self.intervals[index+1].start:
            self.intervals[index+1].start = val
        else:
            self.intervals.insert(index+1, Interval(val, val))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals

    def findIndex(self, val):
        for index in range(len(self.intervals)):
            if self.intervals[index].start > val:
                break

        if self.intervals[index].start > val:
            return index - 1
        else:
            assert index == len(self.intervals) - 1
            return index




# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

# import pydevd
# pydevd.settrace('127.0.0.1', port=55803, stdoutToServer=True, stderrToServer=True)
obj = SummaryRanges()
for val in [1, 3, 7, 2, 6, 4, 3, 3, 8]:
    obj.addNum(val)
    print [(o.start, o.end) for o in obj.getIntervals()]
