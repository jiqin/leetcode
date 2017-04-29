import random


class RandomizedSet(object):

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
        if val in self._map:
            return False
        self._last_index += 1
        if self._last_index >= len(self._list):
            self._list.extend([None] * 1000)
        self._list[self._last_index] = val
        self._map[val] = self._last_index
        return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self._map:
            return False
        index = self._map.pop(val)
        value = self._list[self._last_index]
        if index != self._last_index:
            self._list[index] = value
            self._map[value] = index
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
            if self._rand_index > self._last_index:
                self._rand_index = 0
            value = self._list[self._rand_index]
            self._rand_index += 1
            return value
            # return self._list[self._rand.randint(0, self._last_index)]


obj = RandomizedSet()
for i in range(100):
    assert obj.insert(i)
for i in range(100):
    assert not obj.insert(i)
for i in range(100):
    assert obj.remove(i)
for i in range(100):
    assert not obj.remove(i)
assert obj.getRandom() is None

for i in range(100):
    assert obj.insert(i)

import datetime
t1 = datetime.datetime.now()
count = [0] * 100
for i in range(1000000):
    count[obj.getRandom()] += 1
t2 = datetime.datetime.now()
print 'time:', (t2-t1).total_seconds()
print count

obj = RandomizedSet()
print obj.insert(1)
print obj.insert(1)
print obj.remove(1)
print obj.getRandom()

import timeit
timeit.repeat()
