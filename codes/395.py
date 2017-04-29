import copy


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        indexes = [0] * 26
        for c in s:
            indexes[self.get_index(c)] += 1
        r = self.get_longest_sub_string(s, 0, len(s), k, self.get_invalid_char_set(indexes, k, set()))
        return len(r)

    def get_longest_sub_string(self, s, start, end, k, invalid_char_set):
        # print start, end, s[start:end], invalid_char_set
        """

        :param s: string
        :param k: int
        :param invalid_char_set: set
        :return:
        """
        if start >= end:
            return ''

        result = ''
        indexes = [0] * 26
        tmp_start = start
        for i in range(start, end):
            if s[i] in invalid_char_set:
                tmp_result = self.get_longest_sub_string(
                    s, tmp_start, i, k, self.get_invalid_char_set(indexes, k, invalid_char_set))
                if len(result) < len(tmp_result):
                    result = tmp_result
                indexes = [0] * 26
                tmp_start = i + 1
            else:
                indexes[self.get_index(s[i])] += 1

        if tmp_start == start:
            tmp_result = s[start:end]
        else:
            tmp_result = self.get_longest_sub_string(
                s, tmp_start, end, k, self.get_invalid_char_set(indexes, k, invalid_char_set))
        if len(result) < len(tmp_result):
            result = tmp_result
        return result

    def get_index(self, c):
        return ord(c) - ord('a')

    def get_char(self, index):
        return chr(index + ord('a'))

    def get_invalid_char_set(self, indexes, k, invalid_char_set):
        """

        :param indexes: list of indexes
        :param k: int
        :param invalid_char_set: set of char
        :return:
        """
        result = copy.copy(invalid_char_set)
        for i in range(len(indexes)):
            if 0 < indexes[i] < k:
                result.add(self.get_char(i))
        return result


for s, k in [
    # ('ababbc', 2),
    # ('abaebbcdddzabdacybbbbaaaeaaccddxae', 3),
    # ('ababacb', 3),
    ('aaabb', 3)
]:
    print Solution().longestSubstring(s, k)
