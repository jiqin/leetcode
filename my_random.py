from random import Random
from time import time


class RealRandom(object):
    def __init__(self, rate=0.5, seed=None):
        self._rate = max(0.0, min(1.0, rate))

        if seed is None:
            seed = time()
        self._r = Random(seed)

    def next(self):
        v = self._r.random()
        return v <= self._rate


class FakeRandom(object):
    def __init__(self, rate=0.5, seed=None):
        self._rate = max(0.0, min(1.0, rate))

        if seed is None:
            seed = time()
        self._r = Random(seed)

        self._cur_rate = self._rate

    def next(self):
        v = self._r.random()
        if v <= self._cur_rate:
            self._cur_rate = self._rate
            return True

        self._cur_rate *= 2
        return False


def test(random_obj):
    COUNT = 1000000
    s_index = -1
    s_counts = []

    for i in range(COUNT):
        v = random_obj.next()
        if v:
            s_counts.append(i - s_index)
            s_index = i

    s_counts.sort()

    results = []
    results.append('{:.2f}'.format(len(s_counts) * 1.0 / COUNT))
    results.append('{:.2f}'.format(sum(s_counts) * 1.0 / len(s_counts)))
    for tp in (0, 10, 20, 30, 50, 80, 90):
        index = len(s_counts) * tp / 100
        results.append(s_counts[index])
    results.append(s_counts[-1])

    return results


if __name__ == '__main__':
    def _print(l):
        print ' '.join(map(lambda v: '{:>6}'.format(v), l))

    msg = ['input', 'rate', 'avg']
    for tp in (0, 10, 20, 30, 50, 80, 90):
        msg.append('tp' + str(tp))
    msg.append('max')
    _print(msg)

    clz = RealRandom
    for rate in (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 0.8):
        _print([rate] + test(clz(rate)))

    print '-' * 100
    clz = FakeRandom
    for rate in range(1, 30, 1):
        rate = rate * 1.0 / 100
        _print([rate] + test(clz(rate)))
