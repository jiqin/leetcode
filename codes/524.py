class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        def _cmp_word(w1, w2):
            if len(w1) > len(w2):
                return -1
            elif len(w1) < len(w2):
                return 1
            if w1 < w2:
                return -1
            return 1

        d.sort(cmp=_cmp_word)

        for s1 in d:
            if self._is_ret(s, s1):
                return s1
        return ''

    def _is_ret(self, w1, w2):
        i = 0
        j = 0
        while i < len(w1) and j < len(w2):
            if w1[i] == w2[j]:
                j += 1
            i += 1

        return j >= len(w2)


from my_algorithm.common_test import run_test_cases

run_test_cases(
    Solution().findLongestWord,
    (("abpcplea", ["ale", "apple", "monkey", "plea"], "apple"),
     ("abpcplea", ["a", "b", "c"], 'a'),
     ("aaa", ["a", "aa", "aaa"], 'aaa'),
     ("aaa", ["aaa", "aa", "a"], 'aaa')),
)
