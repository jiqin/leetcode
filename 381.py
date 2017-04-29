import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._map = {}
        self._last_index = -1
        self._list = [None] * 10000
        self._rand = random.Random()
        self._rand_index = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self._last_index += 1
        if self._last_index >= len(self._list):
            self._list.extend([None] * 1000)
        self._list[self._last_index] = val

        index_list = self._map.setdefault(val, [])
        index_list.append(self._last_index)
        return len(index_list) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        index_list = self._map.get(val, [])
        if not index_list:
            return False

        index = index_list.pop(-1)
        if not index_list:
            self._map.pop(val)

        last_value = self._list[self._last_index]
        if index != self._last_index:
            self._list[index] = last_value
            tmp_index_list = self._map[last_value]
            tmp_index_list.remove(self._last_index)
            tmp_index_list.append(index)

        self._last_index -= 1
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if self._last_index < 0:
            return None
        elif self._last_index == 0:
            return self._list[self._last_index]
        else:
            return self._list[self._rand.randint(0, self._last_index)]


obj = RandomizedCollection()
for i in range(100):
    assert obj.insert(i)
for i in range(100):
    assert not obj.insert(i)
for i in range(100):
    assert not obj.insert(i)
for i in range(100):
    assert obj.remove(i)
for i in range(100):
    assert obj.remove(i)
for i in range(100):
    assert obj.remove(i)
for i in range(100):
    assert not obj.remove(i)
assert obj.getRandom() is None

for i in range(100):
    assert obj.insert(i)
for i in range(100):
    assert not obj.insert(0)

import datetime
t1 = datetime.datetime.now()
count = [0] * 100
for i in range(1000000):
    count[obj.getRandom()] += 1
t2 = datetime.datetime.now()
print 'time:', (t2-t1).total_seconds()
print count

obj = RandomizedCollection()
print obj.insert(0)
print obj.insert(1)
print obj.insert(2)
print obj.insert(3)
print not obj.insert(3)
print obj.remove(2)
print obj.remove(3)
print obj.remove(0)
print obj.getRandom()
