class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        rs = []
        i = 0
        while True:
            pow_10_1 = pow(10, i + 1)
            pow_10_2 = pow(10, i)
            if n < pow_10_2:
                break
            i1 = n % pow_10_1
            i2 = i1 / pow_10_2
            i3 = i1 % pow_10_2
            rs.append((i2, i, i3))

            i += 1

        r = 0
        for i1, pow_10, i2 in rs:
            r1 = self._f1(i1, pow_10)
            if i1 == 1:
                r1 += i2
            r += r1
        return r

    def _f1(self, a, n):
        """ count of digit one of a * 10^n
        e.g. a = 3, n = 4, then it is 30000

        :param a: int
        :param n: int
        :return:
        """
        r = a * self._f2(n)
        if a == 1:
            r += 1
        elif a > 0:
            r += pow(10, n)
        return r

    def _f2(self, n):
        """ count of digit one of (1 * 10^n - 1)
        e.g. n = 3, then it is 1000 - 1 = 999

        :param n:
        :return:
        """
        r = 0
        for i in range(1, n + 1):
            r = 10 * r + pow(10, i - 1)
        return r

    def __init__(self):
        self._cached = {0: 0}
        self._max = 0

    def countDigitTwo(self, n):
        r = self._cached.get(n)
        if r is not None:
            return r

        for i in range(self._max + 1, n + 1):
            r = self._cached[i - 1]
            i1 = i
            while i1 > 0:
                i2 = i1 % 10
                if i2 == 1:
                    r += 1
                i1 /= 10
            self._cached[i] = r

        self._max = max(self._max, n)

        return self._cached[n]


def test():
    s = Solution()
    # for i in range(124):
    #     print i, s.countDigitOne(i)
    for i in range(234564):
        i1 = s.countDigitOne(i)
        i2 = s.countDigitTwo(i)
        if i1 != i2:
            print i, i1, i2
            break
    print 'done'


test()
