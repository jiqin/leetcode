class Heap(object):
    def __init__(self):
        self._values = []
        self._num = 0
        self._map_pos = {}

    def get_max(self):
        if self._num > 0:
            return self._values[0]
        else:
            return 0

    def append(self, v):
        pos = self._num
        if pos < len(self._values):
            self._values[pos] = v
        else:
            self._values.append(v)
        self._num += 1
        self._map_pos.setdefault(v, []).append(pos)

        while pos != 0:
            parent = self._parent(pos)
            if self._values[parent] >= self._values[pos]:
                break

            self._swap(parent, pos)
            pos = parent

    def remove(self, v):
        pos_list = self._map_pos[v]
        pos = pos_list.pop(-1)
        assert 0 <= pos < self._num
        if not pos_list:
            self._map_pos.pop(v)
        self._num -= 1

        if pos == self._num:
            return

        self._values[pos] = self._values[self._num]
        self._map_pos[self._values[pos]][-1] = pos

        while True:
            next_pos = pos
            i = self._left(pos)
            if i < self._num and self._values[i] > self._values[next_pos]:
                next_pos = i
            i = self._right(pos)
            if i < self._num and self._values[i] > self._values[next_pos]:
                next_pos = i

            if next_pos != pos:
                self._swap(next_pos, pos)
                pos = next_pos
            else:
                break

    def _parent(self, i):
        return (i - 1) / 2

    def _left(self, i):
        return i * 2 + 1

    def _right(self, i):
        return i * 2 + 2

    def _swap(self, pos1, pos2):
        v1 = self._values[pos1]
        v2 = self._values[pos2]

        self._values[pos1], self._values[pos2] = v2, v1

        p1 = self._map_pos[v1]
        p1.remove(pos1)
        p1.append(pos2)
        p1.sort()

        p2 = self._map_pos[v2]
        p2.remove(pos2)
        p2.append(pos1)
        p2.sort()


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return []

        new_buildings = self.pre_handle(buildings)
        # print new_buildings

        result = []
        heap = Heap()
        for pos, h in new_buildings:
            if h > 0:
                heap.append(h)
            else:
                heap.remove(-h)
            # print h, heap._values[0:heap._num], heap._map_pos
            if not result or result[-1][0] != pos:
                result.append((pos, heap.get_max()))
            else:
                result[-1] = (pos, heap.get_max())

        r = []
        r.append(result[0])
        for v in result[1:]:
            if v[1] != r[-1][1]:
                r.append(v)
        return r

    def pre_handle(self, buildings):
        results = []
        for l, r, h in buildings:
            results.append((l, h))
            results.append((r, -h))

        results.sort(key=lambda v: v[0])
        return results


def test():
    for buildings in (
            ([0,2,3], [2,5,3]),
            # ([2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]),
            # ([2, 9, 10], [3, 7, 10], [5, 12, 12], [15, 20, 10], [19, 24, 8]),
    ):
        print Solution().getSkyline(buildings)


test()
