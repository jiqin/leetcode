# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Heap(object):
    def __init__(self):
        self._values = []
        self._num = 0

    def add(self, l):
        if len(self._values) == self._num:
            self._values.append(l)
        else:
            self._values[self._num] = l
        self._num += 1

        cur = self._num - 1
        while cur > 0:
            parent = self._parent(cur)
            if self._move_left_to_head(cur, parent):
                self._values[parent], self._values[cur] = self._values[cur], self._values[parent]
                cur = parent
            else:
                break

    def pop_head(self):
        if self._num == 0:
            return None

        value = self._values[0]

        self._num -= 1
        self._values[0] = self._values[self._num]

        cur = 0
        while cur < self._num:
            next = cur
            i = self._left(cur)
            if i < self._num and self._move_left_to_head(i, next):
                next = i
            i = self._right(cur)
            if i < self._num and self._move_left_to_head(i, next):
                next = i

            if next == cur:
                break
            self._values[next], self._values[cur] = self._values[cur], self._values[next]
            cur = next

        return value

    def _move_left_to_head(self, l, r):
        return self._values[l].val < self._values[r].val

    def _parent(self, i):
        return (i - 1) / 2

    def _left(self, i):
        return i * 2 + 1

    def _right(self, i):
        return i * 2 + 2


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = Heap()
        for l in lists:
            if l:
                heap.add(l)

        r = ListNode(0)
        n = r

        while True:
            l = heap.pop_head()
            if not l:
                break
            n.next = ListNode(l.val)
            n = n.next

            l = l.next
            if l:
                heap.add(l)

        return r.next


def test():
    def _to_list_node(values):
        head = ListNode(values[0])
        l = head
        for v in values[1:]:
            l.next = ListNode(v)
            l = l.next
        return head

    def _to_list(head):
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l

    for lists in (
            (
                    _to_list_node(range(10)),
                    _to_list_node(range(20)),
                    _to_list_node(range(30)),
                    _to_list_node(range(4, 25)),
            ),
    ):
        print _to_list(Solution().mergeKLists(lists))


test()
