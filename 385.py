# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger(object):
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self._value = value
        self._list = []
        self._is_int = True if value is not None else False

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self._is_int

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        assert self._is_int is False
        self._list.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        assert self._is_int is True
        self._value = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        assert self._is_int is True
        return self._value

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        assert self._is_int is False
        return self._list

    def __repr__(self):
        if self._is_int is True:
            return str(self._value)
        else:
            return '[{}]'.format(','.join(map(str, self._list)))


class Solution(object):
    class Status(object):
        START = 1
        PARSE_LIST_START = 2
        PARSE_LIST_END = 3
        PARSE_NUM = 4
        PARSE_COMMA = 5
        END = 100

    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

        if not s:
            return None

        obj_list = []
        value = ''
        only_one_integer = False
        status = Solution.Status.START

        for i, c in enumerate(s):
            if status in [Solution.Status.START,
                          Solution.Status.PARSE_LIST_START,
                          Solution.Status.PARSE_COMMA]:
                status, obj_list, value, only_one_integer = \
                    self.handle_next_new_item(status, obj_list, value, i, c, only_one_integer)
            elif status == Solution.Status.PARSE_NUM:
                if self.is_num_item(c):
                    value += c
                    continue

                obj_list[-1].add(NestedInteger(int(value)))

                status = self.handle_end_cur_item(only_one_integer, i, c)
            elif status == Solution.Status.PARSE_LIST_END:
                obj_list.pop(-1)
                status = self.handle_end_cur_item(only_one_integer, i, c)
            else:
                raise RuntimeError('{} : {}'.format(i, c))

        if only_one_integer:
            assert status == Solution.Status.PARSE_NUM
            return NestedInteger(int(value))
        else:
            assert status == Solution.Status.PARSE_LIST_END
            assert len(obj_list) == 1
            return obj_list[0]

    def handle_next_new_item(self, status, obj_list, value, i, c, only_one_integer):
        assert status in [Solution.Status.START,
                          Solution.Status.PARSE_LIST_START,
                          Solution.Status.PARSE_COMMA]

        if status != Solution.Status.START:
            assert not only_one_integer

        if c == '[':
            obj = NestedInteger()
            if status != Solution.Status.START:
                obj_list[-1].add(obj)
            obj_list.append(obj)
            status = Solution.Status.PARSE_LIST_START
        elif self.is_num_item(c):
            if status == Solution.Status.START:
                only_one_integer = True
            value = c
            status = Solution.Status.PARSE_NUM
        elif c == ']':
            assert status == Solution.Status.PARSE_LIST_START
            status = Solution.Status.PARSE_LIST_END
        else:
            raise RuntimeError('{} : {}'.format(i, c))

        return status, obj_list, value, only_one_integer

    def handle_end_cur_item(self, only_one_integer, i, c):
        assert not only_one_integer
        if c == ',':
            status = Solution.Status.PARSE_COMMA
        elif c == ']':
            status = Solution.Status.PARSE_LIST_END
        else:
            raise RuntimeError('{} : {}'.format(i, c))
        return status

    def is_num_item(self, c):
        return c in '-0123456789'


for s in ['123', '[]', '[[]]', '[123,[456,[789],-11],-44,33,[44]]']:
    r = Solution().deserialize(s)
    print r
    assert str(r) == s
