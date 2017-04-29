class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[i] == s[j]:
                j += 1

            n = 1
            while True:
                l = i - n
                r = j + n - 1
                if l < 0 or r >= len(s) or s[l] != s[r]:
                    break
                n += 1
            n -= 1
            if len(result) < (2 * n + j - i):
                result = s[i-n:j+n]
            i = j
        return result


print Solution().longestPalindrome('abcdabcdssadmadfasdsdbcccccbadfasldfjsdcbfjdskalmmasdfas')
