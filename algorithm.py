class Heap(object):
    """ A Heap object
    """
    def __init__(self, cmp=lambda v1, v2: v1 <= v2, reserve_size=1000):
        self._value_list = [None] * reserve_size
        self._size = 0
        self._cmp = cmp

    def insert(self, v):
        if self._size == len(self._value_list):
            self._value_list.extend([None] * self._size)
        n = self._size
        self._size += 1
        self._value_list[n] = v

        while n > 0:
            p = self._parent(n)
            if self._cmp(self._value_list[p], self._value_list[n]):
                break
            self._value_list[p], self._value_list[n] = self._value_list[n], self._value_list[p]
            n = p

    def peek(self):
        return self._value_list[0]

    def pop(self):
        if self._size == 0:
            raise UnboundLocalError()

        result = self._value_list[0]
        self._size -= 1
        if self._size == 0:
            return result

        self._value_list[0] = self._value_list[self._size]
        p = 0

        while p < self._size:
            n = p
            l = self._left(p)
            r = self._right(p)

            if l < self._size:
                if not self._cmp(self._value_list[n], self._value_list[l]):
                    n = l

            if r < self._size:
                if not self._cmp(self._value_list[n], self._value_list[r]):
                    n = r

            if n == p:
                break

            self._value_list[p], self._value_list[n] = self._value_list[n], self._value_list[p]
            p = n
        return result

    def get_size(self):
        return self._size

    def _parent(self, n):
        return (n-1) / 2

    def _left(self, n):
        return n * 2 + 1

    def _right(self, n):
        return n * 2 + 2

    def print_me(self):
        return ','.join(map(str, self._value_list[0:self._size]))


def find_first_item_in_list(values, cmp, lbound=None, rbound=None):
    """
    cmp is a function should return -1, 0, 1
    if cmp < 0: in left part
    if cmp = 0: find
    if cmp > 0: in right part
    """
    l = 0 if lbound is None else lbound
    r = len(values) if rbound is None else rbound
    if l == r:
        return None

    r -= 1
    while l < r:
        m = (l + r) / 2
        v = values[m]
        if cmp(v) <= 0:
            r = m
        else:
            l = m + 1
    if cmp(values[r]) == 0:
        return r
    else:
        return None


def find_last_item_in_list(values, cmp, lbound=None, rbound=None):
    """
    cmp is a function should return -1, 0, 1
    if cmp < 0: in left part
    if cmp = 0: find
    if cmp > 0: in right part
    """
    l = 0 if lbound is None else lbound
    r = len(values) if rbound is None else rbound
    if l == r:
        return None

    while l < r - 1:
        m = (l + r) / 2
        v = values[m]
        if cmp(v) < 0:
            r = m
        else:
            l = m
    if cmp(values[l]) == 0:
        return l
    else:
        return None


def find_last_less_equal(values, v, l=None, r=None):
    """
    Return index of the latest less or equal value of v
    values: [1, 3, 5, 7, 9]
    if v = 8, return 3
    if v = 7, return 3
    if v = 6, return 2
    if v = -1, return None
    """
    def cmp(v1):
        if v1 <= v:
            return 0
        else:
            return -1

    return find_last_item_in_list(values, cmp, l, r)


def test_find_latest_less_equal():
    values = [1, 3, 5, 7, 9]
    test_cases = {-1: None, 0: None, 1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 4, 10: 4, 11: 4}
    for v, r1 in test_cases.iteritems():
        r2 = find_last_less_equal(values, v)
        if r1 != r2:
            print 'test_find_latest_less_equal Fail: v: {}, {} != {}'.format(v, r1, r2)


def find_value_in_sum_list(values, v):
    def _(r, sums, v1, results):
        if v1 == 0:
            return results
        if r <= 0:
            return None
        if sums[r-1] < v1:
            return None

        i = find_last_less_equal(values, v1, 0, r)
        if i is None:
            return None
        results.append(i)
        tmpr = _(i, sums, v1 - values[i], results)
        if tmpr:
            return tmpr
        results.pop()
        return _(i, sums, v1, results)

    def _sum():
        if len(values) == 0:
            return []
        _sums = [values[0]]
        for _v in values[1:]:
            _sums.append(_sums[-1] + _v)
        return _sums

    return _(len(values), _sum(), v, [])


def test_is_value_in_sum_list():
    values = [1, 1, 2, 8, 100, 101, 102]
    test_cases = {
        1: [1],
        2: [2],
        3: [1, 2],
        4: [0, 1, 2],
        5: None,
        6: None,
        7: None,
        8: [3],
        9: [1, 3],
        10: [2, 3],
        99: None,
        100: [4],
        101: [5],
        102: [6],
        103: [1, 6],
        1000: None
    }
    for v, r1 in test_cases.iteritems():
        r2 = find_value_in_sum_list(values, v)
        if r2:
            r2.sort()
        if r1 != r2:
            print 'test_is_value_in_sum_list Fail: v: {}, {} != {}'.format(v, r1, r2)


if __name__ == '__main__':
    from importlib import import_module
    module = import_module(__name__)
    for attr in dir(module):
        if attr.startswith('test_'):
            print 'run', attr
            f = getattr(module, attr)
            f()

