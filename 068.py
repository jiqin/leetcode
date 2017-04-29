class Solution(object):
    def fullJustify1(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        # This  is  a  new word of
        # start = 0
        # end = 6
        # word_count = 6
        # width_diff = 3
        # min_space_num = 1
        # max_space_count = 3
        results = []
        start = 0
        while start < len(words):
            end = start
            size = len(words[end])
            while size <= maxWidth:
                end += 1
                if end >= len(words):
                    break
                size += 1 + len(words[end])

            if size > maxWidth:
                size -= 1 + len(words[end])

            word_count = end - start
            assert word_count > 0

            width_diff = maxWidth - size
            assert width_diff >= 0

            s = ''
            if end == len(words):
                s += words[start]
                for i in range(start + 1, end):
                    s += ' '
                    s += words[i]
                s += ' ' * (maxWidth - len(s))
            elif word_count == 1:
                s += words[start]
                s += ' ' * width_diff
            else:
                min_space_num = width_diff / (word_count - 1) + 1
                max_space_count = width_diff % (word_count - 1)

                for i in range(start, start + max_space_count):
                    s += words[i]
                    s += ' ' * (min_space_num + 1)
                s += words[start + max_space_count]
                for i in range(start + max_space_count + 1, end):
                    s += ' ' * min_space_num
                    s += words[i]

            results.append(s)
            start = end
        return results

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        cur_words = []
        cur_len = 0
        for w in words:
            if cur_len + len(cur_words) + len(w) > maxWidth:
                result.append(self._justify(cur_words, maxWidth - cur_len))
                cur_words = []
                cur_len = 0
            cur_words.append(w)
            cur_len += len(w)
        result.append(' '.join(cur_words) + ' ' * (maxWidth - cur_len - len(cur_words) + 1))
        return result

    def _justify(self, words, space_len):
        if len(words) == 1:
            return words[0] + ' ' * space_len

        n1 = space_len / (len(words) - 1)
        n2 = space_len - n1 * (len(words) - 1)

        r = ''
        for i in range(0, n2):
            r += words[i] + ' ' * (n1 + 1)
        for i in range(n2, len(words) - 1):
            r += words[i] + ' ' * n1
        r += words[-1]
        return r

        return ' '.join(words)


from my_algorithm.common_test import run_test_cases


run_test_cases(
    Solution().fullJustify,
    (
        (
            ["This", "is", "an", "example", "of", "text", "justification.", 'aaa', 'bbb'],
            16,
            ['This    is    an',
             'example  of text',
             'justification.  ',
             'aaa bbb         ',
             ],
        ),
    ),
)
