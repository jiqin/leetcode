class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        # key: index
        # value: List[str], result of s[index:]
        cached_result = {}
        self._break(s, 0, wordDict, cached_result)

        return cached_result[0]

    def _break(self, s, index, wordDict, cached_result):
        """
        Get result of s[index:]

        :param s: str
        :param index: int, index of s
        :param wordDict: Set[str]
        :param cached_result: List[str], result of s[m:]
        :return:
        """
        result = cached_result.get(index)
        if result is not None:
            return

        result = []
        for i in range(index + 1, len(s) + 1):
            w = s[index:i]
            if w in wordDict:
                if i == len(s):
                    result.append(w)
                else:
                    self._break(s, i, wordDict, cached_result)
                    tmp_result = cached_result[i]
                    for tmp_s in tmp_result:
                        result.append('{} {}'.format(w, tmp_s))
        cached_result[index] = result


for s, w in (
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
):
    r = Solution().wordBreak(s, w)
    print '\n'.join(r)
    # print r
