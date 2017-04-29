class Solution(object):
    def findSubstring1(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        elif len(s) < len(words[0]):
            return []

        # example: {'foo': 0, 'bar': 1}
        words_index_mapping = {}
        for w in words:
            if w not in words_index_mapping:
                words_index_mapping[w] = len(words_index_mapping)
        # example: [1, 1]
        words_index_count = [0] * len(words_index_mapping)
        for w in words:
            words_index_count[words_index_mapping[w]] += 1

        # example: [1, -1, -1, 0, -1, -1, -1, -1, -1, 0, -1, -1, 1, -1, -1, -1]
        s_index = [-1] * (len(s) - len(words[0]) + 1)
        for i in range(len(s_index)):
            s_index[i] = words_index_mapping.get(s[i:i + len(words[0])], -1)
        # print words_index_mapping
        # print words_index_count
        # print s_index

        results = []
        for start in range(len(words[0])):
            # example: [1, 0]
            cur_words_index_count = [0] * len(words_index_count)
            for i in range(start, len(s_index), len(words[0])):
                i1 = i - len(words[0]) * len(words)
                if i1 >= 0 and s_index[i1] >= 0:
                    cur_words_index_count[s_index[i1]] -= 1
                if s_index[i] >= 0:
                    cur_words_index_count[s_index[i]] += 1
                    find_result = (cur_words_index_count == words_index_count)
                    if find_result:
                        results.append(i - len(words[0]) * (len(words) - 1))
                        # print i1, i, cur_words_index_count

        return results

    def findSubstring(self, s, words):
        results = []

        if len(s) == 0 or len(words) == 0:
            return results

        from collections import defaultdict

        len_word = len(words[0])
        word_count, words_count_map = len(words), defaultdict(lambda: 0)

        if len(s) < word_count * len_word:
            return results

        for w in words:
            words_count_map[w] += 1

        for start_index in range(0, len_word, len_word):
            cur_words_count, cur_words_count_map = 0, defaultdict(lambda: 0)

            for cur_index in range(start_index, len(s), len_word):
                if cur_index + len_word >= len(s):
                    break

                cur_word = s[cur_index:cur_index + len_word]
                if cur_word not in words_count_map:
                    cur_words_count, cur_words_count_map = 0, defaultdict(lambda: 0)
                    continue

                cur_words_count += 1
                cur_words_count_map[cur_word] += 1

                while cur_words_count_map[cur_word] > words_count_map[cur_word]:
                    first_index = cur_index - len_word * (cur_words_count - 1)
                    first_word = s[first_index:first_index + len_word]
                    cur_words_count -= 1
                    cur_words_count_map[first_word] -= 1

                if cur_words_count == word_count:
                    results.append(cur_index - len_word * (cur_words_count - 1))

        return results

    def _pop_first_word(self, s, len_word, cur_index, cur_words_count, cur_words_count_map):
        first_index = cur_index - len_word * (cur_words_count - 1)
        first_word = s[first_index:first_index + len_word]
        cur_words_count -= 1
        cur_words_count_map[first_word] -= 1
        return cur_words_count, cur_words_count_map


from my_algorithm.common_test import run_test_cases

run_test_cases(
    Solution().findSubstring,
    (
        ('barfoothefoobarman', ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "good"], [8]),
    ),
)
