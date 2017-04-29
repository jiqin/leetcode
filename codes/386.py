class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        results = [None] * n
        v = 1
        results[0] = v
        for i in range(n-1):
            v = self.get_next(v, n)
            results[i + 1] = v
        return results

    def get_next(self, i, n):
        i1 = i * 10
        if i1 <= n:
            return i1
        i2 = i + 1
        if i2 > n:
            i2 = i / 10
            i2 += 1

        while i2 % 10 == 0:
            i2 /= 10
        return i2


from collections import defaultdict
n = 14959
l = Solution().lexicalOrder(n)
assert len(l) == n

v = {}
for i in l:
    v[i] = v.get(i, 0) + 1
for i, m in v.iteritems():
    if m != 1 or i > n:
        print i, m

for i in range(1, n+1):
    if i not in v:
        print i

for i in range(len(l) - 1):
    v1 = l[i]
    v2 = l[i+1]
    if str(v1) >= str(v2):
        print i, v1, v2

enu
