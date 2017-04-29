class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        cached = {}
        return self._is_match(s, 0, p, 0, cached)

    def _is_match(self, s, i, p, j, cached):
        """

        :param s: str
        :param i: int
        :param p: str
        :param j: int
        :param cached: dict: (int, int) => bool
        :return: bool
        """
        r = cached.get((i, j))
        if r is not None:
            return r

        if i == len(s):
            while j < len(p):
                if j + 1 < len(p) and p[j + 1] == '*':
                    j += 2
                else:
                    break
            return j == len(p)
        if j == len(p):
            return False

        if j + 1 < len(p) and p[j + 1] == '*':
            r = self._is_match(s, i, p, j + 2, cached)
            if not r:
                for i1 in range(i, len(s)):
                    if p[j] == '.' or s[i1] == p[j]:
                        r = self._is_match(s, i1 + 1, p, j + 2, cached)
                        if r:
                            break
                    else:
                        r = False
                        break
            cached[(i, j)] = r
            return r

        if p[j] == '.' or s[i] == p[j]:
            r = self._is_match(s, i + 1, p, j + 1, cached)
        else:
            r = False

        cached[(i, j)] = r
        return r


def test():
    for s, p, r in (
            ("aa", "a", False),
            ("aa", "aa", True),
            ("aaa", "aa", False),
            ("aa", "a*", True),
            ("aa", ".*", True),
            ("ab", ".*", True),
            ("aab", "c*a*b", True),
            ("a", "ab*", True),
    ):
        if Solution().isMatch(s, p) != r:
            print 'Failed:', s, p


test()
