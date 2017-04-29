# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def __repr__(self):
        return '({} {} {})'.format(self.label, self.next.label if self.next else 'X', self.random.label if self.random else 'X')


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        node_map = {}

        new_head = RandomListNode(head.label)
        node_map[head] = new_head

        p1 = head.next
        p2 = new_head
        while p1 is not None:
            p2.next = RandomListNode(p1.label)
            p2 = p2.next
            node_map[p1] = p2
            p1 = p1.next

        p1 = head
        p2 = new_head
        while p1 is not None:
            if p1.random is not None:
                p2.random = node_map[p1.random]
            p1 = p1.next
            p2 = p2.next

        return new_head


def test():
    hs = [RandomListNode(0), RandomListNode(1), RandomListNode(2)]
    hs[0].next = hs[1]
    hs[1].next = hs[2]
    hs[0].random = hs[2]
    hs[2].random = hs[1]

    r = Solution().copyRandomList(hs[0])
    while r:
        print r
        r = r.next


test()

