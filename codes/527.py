class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        str_map = defaultdict(list)
        for s in dict:
            str_map[self._to_abbreviation(s)].append(s)
        # print str_map

        str_map_result = {}
        while len(str_map) > 0:
            k, v = str_map.popitem()
            if k in str_map_result:
                v1 = str_map_result.pop(k)
                v.append(v1)
                str_map[k] = v
            elif len(v) == 1:
                str_map_result[k] = v[0]
            else:
                rs = self._reabbreviation(k, v)
                # print '.', k, v, rs
                str_map.update(rs)

        reversed_map = {}
        for k, v in str_map_result.iteritems():
            reversed_map[v] = k
        return map(lambda w: reversed_map.get(w), dict)

    def _to_abbreviation(self, s):
        if len(s) < 4:
            return s
        else:
            return s[0] + str(len(s) - 2) + s[-1]

    def _reabbreviation(self, k, words):
        ret = {}
        len_0 = len(words[0])
        for i in range(1, len_0 - 3):
            if len(words) == 0:
                break

            from collections import defaultdict
            tmp_ret = defaultdict(list)
            for w in words:
                tmp_ret[w[0:i + 1]].append(w)

            words = []
            for k, v in tmp_ret.iteritems():
                if len(v) == 1:
                    w = v[0]
                    ret[w[0:i + 1] + str(len_0 - i - 2) + w[-1]] = v
                else:
                    words.extend(v)

        for w in words:
            ret[w] = [w]
        return ret


from my_algorithm.common_test import run_test_cases

run_test_cases(
    Solution().wordsAbbreviation,
    (
        (
            ['internal', 'interval'],
            ['internal', 'interval'],
        ),
        (
            ['intension', 'intrusion'],
            ['inte4n', 'intr4n'],
        ),
        (
            ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"],
            ["l2e", "god", "internal", "me", "i6t", "interval", "inte4n", "f2e", "intr4n"]
        ),
    ),
)
