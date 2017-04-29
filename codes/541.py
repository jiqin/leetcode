class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = 0
        s = list(s)
        while i < len(s):
            if i + k < len(s):
                self._reverse(s, i, i + k)
            else:
                self._reverse(s, i, len(s))
            i += 2 * k
        return ''.join(s)

    def _reverse(self, s, start, end):
        end -= 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


from my_algorithm.common_test import run_test_cases


run_test_cases(
    Solution().reverseStr,
    (
        ('1234567890', 2, '2134657809'),
        ('1234567890', 3, '3214569870'),
        ('1234567890', 4, '4321567809'),
        ('1234567890', 9, '9876543210'),
        ('1234567890', 10, '0987654321'),
        ('1234567890', 11, '0987654321'),
    ),
)
