class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        return self._is_interleave(s1, 0, s2, 0, s3, {})

    def _is_interleave(self, s1, i1, s2, i2, s3, cached):
        r = cached.get((i1, i2))
        if r is not None:
            return r

        i3 = i1 + i2
        r = False

        if i3 == len(s3):
            r = True

        if not r and i1 < len(s1) and s1[i1] == s3[i3]:
            r = self._is_interleave(s1, i1 + 1, s2, i2, s3, cached)

        if not r and i2 < len(s2) and s2[i2] == s3[i3]:
            r = self._is_interleave(s1, i1, s2, i2 + 1, s3, cached)

        cached[(i1, i2)] = r
        return r


def test():
    for s1, s2, s3 in (
            ("aabcc",
             "dbbca",
             "aadbbcbcac"),
            ("aabcc",
             "dbbca",
             "aadbbbaccc"),
    ):
        print Solution().isInterleave(s1, s2, s3)


test()
