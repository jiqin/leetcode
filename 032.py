class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # e.g. [(0, 10), (1, 4), ...]
        valid_pair_list = []
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    i1 =stack.pop(-1)
                    valid_pair_list.append((i1, i))
        valid_pair_list.sort(key=lambda a: a[0])
        if len(valid_pair_list) == 0:
            return 0
        result = 0
        cur_result = 0
        next = 0
        for s, e in valid_pair_list:
            if s < next:
                continue
            elif s == next:
                cur_result += (e - s + 1)
                next = e + 1
            else:
                result = max(result, cur_result)
                cur_result = (e - s + 1)
                next = e + 1
        result = max(result, cur_result)
        return result


for s in (
        (''),
        ('())'),
        ('(()())(()'),
        ('(()())(())'),
        ('(()())(()))()('),
):
    print Solution().longestValidParentheses(s)
