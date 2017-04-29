class Solution(object):
    def get_letter_index_mapping(self, s):
        # {letter: [index]}
        # e.g. {'a': [0, 3], 'b':[1], ...}
        letter_index_mapping = {}
        for i, c in enumerate(s):
            letter_index_mapping.setdefault(c, []).append(i)
        return letter_index_mapping

    def removeDuplicateLetters(self, s):
        """

        :param s: str
        :return: str
        """
        if len(s) <= 1:
            return s

        letter_index_mapping = self.get_letter_index_mapping(s)

        # [('a', [0, 5, 6]), ...]
        letter_indexes = [(letter, indexes) for letter, indexes in letter_index_mapping.iteritems()]
        letter_indexes.sort(key=lambda li: li[0])

        result = ''

        while letter_indexes:
            min_last_index = min(map(lambda li: li[1][-1], letter_indexes))

            i = 0
            for i, letter_index in enumerate(letter_indexes):
                index0 = letter_index[1][0]
                if index0 <= min_last_index:
                    break

            result += letter_index[0]
            index0 = letter_index[1][0]
            letter_indexes.pop(i)

            for letter, indexes in letter_indexes:
                while indexes and indexes[0] < index0:
                    indexes.pop(0)

        return result


def test():
    for input, result in (
            ('bcabc', 'abc'),
            ('cbacdcbc', 'acdb'),
            ('bcab', 'bca'),
            ('cbaddabaa', 'cadb'),
            ('eywdgenmcnzhztolafcfnirfpuxmfcenlppegrcalgxjlajxmphwidqqtrqnmmbssotoywfrtylm',
             'chzafipuegjlxdqnbsotwrym'),
    ):
        r = Solution().removeDuplicateLetters(input)
        if r != result:
            print '>>>>>> Fail:', input, result, r
        else:
            print 'Pass:', input, result


if __name__ == '__main__':
    test()
