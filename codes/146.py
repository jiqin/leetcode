class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class NodeList(object):
    def __init__(self):
        # _head is the latest used node
        self._head = Node(None, None)
        self._tail = Node(None, None)
        self._head.next = self._tail
        self._tail.prev = self._head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_to_head(self, node):
        node.prev = self._head
        node.next = self._head.next
        node.prev.next = node
        node.next.prev = node

    def remove_tail_node(self):
        node = self._tail.prev
        self.remove(node)
        return node


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._node_list = NodeList()
        self._map = {}
        self._capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        node = self._map.get(key)
        if node is None:
            return -1
        assert node.key == key
        self._node_list.remove(node)
        self._node_list.insert_to_head(node)
        return node.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        node = self._map.get(key)
        if node:
            assert node.key == key
            self._node_list.remove(node)

        node = Node(key, value)
        self._node_list.insert_to_head(node)
        self._map[key] = node

        if len(self._map) > self._capacity:
            last_node = self._node_list.remove_tail_node()
            assert last_node.key in self._map
            self._map.pop(last_node.key)


lru = LRUCache(10)
for i in range(100):
    lru.set(i, i)
    print '0', lru.get(0)
    print i, lru.get(i)
