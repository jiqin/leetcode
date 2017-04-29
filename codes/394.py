class BaseItem(object):
    pass


class StringItem(BaseItem):
    def __init__(self, s):
        self._s = s

    def __repr__(self):
        return self._s


class GroupItem(BaseItem):
    def __init__(self, count):
        self._count = count
        self._sub_item_list = []

    def add_item(self, item):
        self._sub_item_list.append(item)

    def __repr__(self):
        return ''.join([''.join(map(str, self._sub_item_list))] * self._count)


class Solution(object):
    class Status(object):
        START = 1
        END = 2
        PARSE_STR = 3
        PARSE_NUM = 4
        START_GROUP = 5
        END_GROUP = 6

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        status = Solution.Status.START
        items = []
        item_stack = []
        num_str = ''
        value_str = ''

        for i, c in enumerate(s):
            if status == Solution.Status.START:
                if c.islower():
                    value_str = c
                    status = Solution.Status.PARSE_STR
                elif c.isdigit():
                    num_str = c
                    status = Solution.Status.PARSE_NUM
                else:
                    raise Exception('{}: {}'.format(i, c))
            elif status == Solution.Status.PARSE_STR:
                if c.islower():
                    value_str += c
                elif c in ']' or c.isdigit():
                    item = StringItem(value_str)
                    value_str = ''
                    if item_stack:
                        item_stack[-1].add_item(item)
                    else:
                        items.append(item)
                    if c == ']':
                        status = Solution.Status.END_GROUP
                    else:
                        num_str = c
                        status = Solution.Status.PARSE_NUM
                else:
                    raise Exception('{}: {}'.format(i, c))
            elif status == Solution.Status.PARSE_NUM:
                if c.isdigit():
                    num_str += c
                elif c in '[':
                    item = GroupItem(int(num_str))
                    num_str = ''
                    if item_stack:
                        item_stack[-1].add_item(item)
                    else:
                        items.append(item)
                    item_stack.append(item)
                    status = Solution.Status.START_GROUP
                else:
                    raise Exception('{}: {}'.format(i, c))
            elif status == Solution.Status.START_GROUP:
                if c.islower():
                    value_str = c
                    status = Solution.Status.PARSE_STR
                elif c.isdigit():
                    num_str = c
                    status = Solution.Status.PARSE_NUM
                else:
                    raise Exception('{}: {}'.format(i, c))
            elif status == Solution.Status.END_GROUP:
                item_stack.pop(-1)
                if c in ']':
                    continue
                elif c.islower():
                    value_str = c
                    status = Solution.Status.PARSE_STR
                elif c.isdigit():
                    num_str = c
                    status = Solution.Status.PARSE_NUM
                else:
                    raise Exception('{}: {}'.format(i, c))

        if status == Solution.Status.PARSE_STR:
            items.append(StringItem(value_str))
        elif status == Solution.Status.END_GROUP:
            item_stack.pop(-1)
        else:
            raise Exception()
        assert len(item_stack) == 0
        return ''.join(map(str, items))


for s in ['2[abc]3[cd]ef',
          '3[a]2[bc]',
          '3[a2[c]]',
          ]:
    print Solution().decodeString(s)
