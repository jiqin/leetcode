# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        import random
        self._head = head
        self._cur = head
        self._rand = random.Random()

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        while True:
            if self._rand.randint(0, 1) == 0:
                return self._cur.val
            else:
                self._cur = self._cur.next
                if not self._cur:
                    self._cur = self._head


# Your Solution object will be instantiated and called as such:
head = ListNode(0)
cur = head
cur.next = ListNode(1)
cur = cur.next
cur.next = ListNode(2)
cur = cur.next
obj = Solution(head)

values = [0] * 3
for i in range(10000):
    values[obj.getRandom()] += 1
print values