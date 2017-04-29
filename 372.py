class Solution(object):
    def superPow(self, a, b):
        """
        a ^ (b + c) = (a ^ b) * (a ^ c)
        a ^ (b * c) = (a ^ b) ^ c
                    = (a ^ c) ^ b

        so
        a ^ (b0 * 10 ^ (n-1) + b1 * 10 ^ (n-2) + ... + bn-1 * 10 ^ 0) =
        ((a ^ 10) ^ (n-1)) ^ b0 *
        ((a ^ 10) ^ (n-2)) ^ b1 *
        ...
        ((a ^ 10) ^ 0) ^ bn-1

        :type a: int
        :type b: List[int]
        :rtype: int
        """
        c = 1337
        r = 1
        cache_a_10_n = {}
        for i, b1 in enumerate(b):
            r1 = self._pow_with_power_10_n(a, len(b) - 1 - i, c, cache_a_10_n)
            r2 = pow(r1, b1) % c
            r = (r * r2) % c
        print cache_a_10_n
        return r

    def _pow_with_power_10_n(self, a, n, c, cache):
        """ return (a ^ 10) ^ n % c

        :param a: int
        :param n: int
        :param c: int
        :param cache: (a, n, c) => value
        :return:
        """
        key = (a, n, c)
        r = cache.get(key)
        if r is None:
            if n == 0:
                r = a % c
            else:
                r = self._pow_with_power_10_n(a, n-1, c, cache)
                r = pow(r, 10) % c
            cache[key] = r
        return r


print Solution().superPow(2, [3])
print Solution().superPow(2, [1, 0])
print Solution().superPow(2, [1, 4, 0, 0])
