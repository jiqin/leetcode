class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_frequency_dict = {}
        for n in nums:
            num_frequency_dict[n] = num_frequency_dict.get(n, 0) + 1

        heap = [(k1, v) for k1, v in num_frequency_dict.iteritems()]
        self.make_heap(heap, k)
        for i in range(k, len(heap)):
            self.add_to_heap(heap, k, heap[i])
        return map(lambda v:v[0], heap[0:k])

    def make_heap(self, heap, size):
        """
        :heap: list of data (num, frequency)
        :size: int, heap size
        """
        for i in range(size):
            c = i
            while c > 0:
                p = self.parent(c)
                if self.correct_heap_relation(heap, p, c):
                    break
                self.swap(heap, p, c)
                c = p

    def correct_heap_relation(self, heap, p, c):
        return heap[p][1] <= heap[c][1]

    def add_to_heap(self, heap, size, v):
        if heap[0][1] > v[1]:
            return

        heap[0] = v
        p = 0
        while p < size:
            l = self.lchild(p)
            r = self.rchild(p)
            if r >= size:
                if l >= size:
                    break
                if self.correct_heap_relation(heap, p, l):
                    break
                self.swap(p, l)
                p = l
            else:
                if self.correct_heap_relation(heap, p, l):
                    if self.correct_heap_relation(heap, p, r):
                        break
                    self.swap(p, r)
                    p = r
                else:
                    if self.correct_heap_relation(heap, p, r):
                        self.swap(p, l)
                        p = l
                    else:
                        if heap[l][1] <= heap[r][1]:
                            self.swap(p, l)
                            p = l
                        else:
                            self.swap(p, r)
                            p = r

    def swap(self, heap, i, j):
        tmp = heap[i]
        heap[i] = heap[j]
        heap[j] = tmp

    def lchild(self, n):
        return n * 2 + 1

    def rchild(self, n):
        return n * 2 + 2

    def parent(self, n):
        return (n - 1) / 2


import pydevd
pydevd.settrace('127.0.0.1', port=55803, stdoutToServer=True, stderrToServer=True)
print Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)