class Heap(object):
    def __init__(self, cmp_left_to_head):
        self._cmp_left_to_head = cmp_left_to_head
        self._values = []

    def head(self):
        return self._values[0] if len(self._values) > 0 else None

    def replace_head(self, value):
        assert len(self._values) > 0
        self._values[0] = value
        cur = 0
        while cur < len(self._values):
            n = cur
            l = self._left(cur)
            if l < len(self._values) and self._cmp_left_to_head(self._values[l], self._values[n]):
                n = l
            r = self._right(cur)
            if r < len(self._values) and self._cmp_left_to_head(self._values[r], self._values[n]):
                n = r
            if n == cur:
                break
            self._values[n], self._values[cur] = self._values[cur], self._values[n]
            cur = n

    def add_value(self, value):
        self._values.append(value)
        cur = len(self._values) - 1
        while cur > 0:
            p = self._parent(cur)
            if self._cmp_left_to_head(self._values[p], self._values[cur]):
                break
            self._values[p], self._values[cur] = self._values[cur], self._values[p]
            cur = p

    def size(self):
        return len(self._values)

    def _parent(self, index):
        assert index > 0
        return (index - 1) / 2

    def _left(self, index):
        return index * 2 + 1

    def _right(self, index):
        return index * 2 + 2


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._left_heap = Heap(lambda a, b: a > b)
        self._right_heap = Heap(lambda a, b: a < b)

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        assert self._left_heap.size() >= self._right_heap.size()
        if self._left_heap.size() == 0:
            self._left_heap.add_value(num)
        elif self._left_heap.size() == self._right_heap.size():
            value = self._right_heap.head()
            if num > value:
                self._right_heap.replace_head(num)
                self._left_heap.add_value(value)
            else:
                self._left_heap.add_value(num)
        else:
            value = self._left_heap.head()
            if num < value:
                self._left_heap.replace_head(num)
                self._right_heap.add_value(value)
            else:
                self._right_heap.add_value(num)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        assert self._left_heap.size() >= self._right_heap.size()
        # print self._left_heap._values, self._left_heap.size(), self._left_heap.head()
        # print self._right_heap._values, self._right_heap.size(), self._right_heap.head()
        if self._left_heap.size() == 0:
            return None
        elif self._left_heap.size() > self._right_heap.size():
            return self._left_heap.head() * 1.0
        else:
            return (self._left_heap.head() + self._right_heap.head()) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
mf = MedianFinder()
for i in range(10):
    mf.addNum(i * -1)
    print mf.findMedian()
