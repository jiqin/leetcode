class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        data_structure = []
        for s in board:
            data_structure.append([])
            for c in s:
                if c == '.':
                    data_structure[-1].append([None, False, set(list(range(1, 10))), [0] * 10])
                else:
                    data_structure[-1].append([int(c), True, None, None])

        for i, j in self.iter_all():
            value, is_fixed, aviable_set, occupy_times = data_structure[i][j]
            if is_fixed:
                can_set = self.try_set_value(data_structure, i, j, value)
                assert can_set

        result = self.handle(data_structure, 0, 0)
        for i, j in self.iter_all():
            board[i][j] = str(data_structure[i][j][0])

    def print_data_structure(self, data_structure):
        print '>' * 100
        for d1 in data_structure:
            print d1[0:3]
            print d1[3:6]
            print d1[6:9]
            print ''

    def handle(self, data_structure, i, j):
        if i is None:
            return True

        value, is_fixed, aviable_set, occupy_times = data_structure[i][j]
        i1, j1 = self.iter_next(i, j)

        if is_fixed:
            return self.handle(data_structure, i1, j1)

        assert value is None
        if len(aviable_set) == 0:
            return False

        aviable_list = list(aviable_set)
        for v in aviable_list:
            try_set =  self.try_set_value(data_structure, i, j, v)
            if try_set:
                data_structure[i][j][0] = v
                r = self.handle(data_structure, i1, j1)
                if r:
                    return r
                data_structure[i][j][0] = None
            self.un_try_set_value(data_structure, i, j, v)

        return False

    def iter_all(self):
        for i in range(9):
            for j in range(9):
                yield i, j

    def iter_next(self, i, j):
        if j < 8:
            return i, j + 1
        elif i < 8:
            return i + 1, 0
        else:
            return None, None

    def iter_prev(self, i, j):
        if j > 0:
            return i, j - 1
        elif i > 0:
            return i - 1, 8
        else:
            return None, None

    def iter_affect_indexs(self, i, j):
        for i1 in range(9):
            if i1 != i:
                yield i1, j
        for j1 in range(9):
            if j1 != j:
                yield i, j1

        istart = i / 3 * 3
        jstart = j / 3 * 3

        for i1 in range(istart, istart + 3):
            for j1 in range(jstart, jstart + 3):
                if not (i1 == i and j1 == j):
                    yield i1, j1

    def try_set_value(self, data_structure, i, j, v):
        assert 0 <= i < 9
        assert 0 <= j < 9
        assert 1 <= v <= 9

        can_set = True
        for i1, j1 in self.iter_affect_indexs(i, j):
            self.remove_value_from_aviable_list(data_structure, i1, j1, v)
            if not self.has_aviable_value(data_structure, i1, j1):
                can_set = False
        return can_set

    def un_try_set_value(self, data_structure, i, j, v):
        for i1, j1 in self.iter_affect_indexs(i, j):
            self.add_value_to_aviable_list(data_structure, i1, j1, v)

    def add_value_to_aviable_list(self, data_structure, i, j, v):
        value, is_fixed, aviable_set, occupy_times = data_structure[i][j]
        if is_fixed:
            return

        assert value != v

        occupy_times[v] -= 1
        if occupy_times[v] == 0:
            aviable_set.add(v)

    def remove_value_from_aviable_list(self, data_structure, i, j, v):
        value, is_fixed, aviable_set, occupy_times = data_structure[i][j]
        if is_fixed:
            return

        # assert value != v

        if v in aviable_set:
            assert occupy_times[v] == 0
            aviable_set.remove(v)

        occupy_times[v] += 1

    def has_aviable_value(self, data_structure, i, j):
        value, is_fixed, aviable_set, occupy_times = data_structure[i][j]
        return is_fixed or len(aviable_set) > 0


def test():
    for board in (
            [
                '53..7....',
                '6..195...',
                '.98....6.',
                '8...6...3',
                '4..8.3..1',
                '7...2...6',
                '.6....28.',
                '...419..5',
                '....8..79'
            ],
            [
                "..9748...",
                "7........",
                ".2.1.9...",
                "..7...24.",
                ".64.1.59.",
                ".98...3..",
                "...8.3.2.",
                "........6",
                "...2759.."
            ]
    ):
        new_borad = []
        for l in board:
            new_borad.append([c for c in l])
        Solution().solveSudoku(new_borad)
        print '\n'.join([''.join(l) for l in new_borad])
        print ''


test()
