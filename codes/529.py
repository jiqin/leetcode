class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        stacks = [click]
        done = set()
        while stacks:
            c = stacks.pop(-1)
            hc = '_'.join(map(str, c))
            if hc in done:
                continue
            done.add(hc)

            rounds = self._find_round_pos(board, c[0], c[1])
            num = self._find_round_mine_count(board, rounds)
            if num > 0:
                board[c[0]][c[1]] = str(num)
            else:
                board[c[0]][c[1]] = 'B'
                stacks.extend(rounds)

        return board

    def _find_round_pos(self, board, x, y):
        rounds = []
        if x > 0:
            if y > 0:
                rounds.append([x - 1, y - 1])
            rounds.append([x - 1, y])
            if y < len(board[0]) - 1:
                rounds.append([x - 1, y + 1])

        if y > 0:
            rounds.append([x, y - 1])
        if y < len(board[0]) - 1:
            rounds.append([x, y + 1])

        if x < len(board) - 1:
            if y > 0:
                rounds.append([x + 1, y - 1])
            rounds.append([x + 1, y])
            if y < len(board[0]) - 1:
                rounds.append([x + 1, y + 1])
        return rounds

    def _find_round_mine_count(self, board, rounds):
        return sum(map(lambda x: self._count_mine(board, x[0], x[1]), rounds))

    def _count_mine(self, board, x, y):
        return 1 if board[x][y] == 'M' else 0


from my_algorithm.common_test import run_test_cases, is_matrix_equal, print_matrix

run_test_cases(
    Solution().updateBoard,
    (
        ([['E', 'E', 'E', 'E', 'E'],
          ['E', 'E', 'M', 'E', 'E'],
          ['E', 'E', 'E', 'E', 'E'],
          ['E', 'E', 'E', 'E', 'E']],
         [3, 0],
         [['B', '1', 'E', '1', 'B'],
          ['B', '1', 'M', '1', 'B'],
          ['B', '1', '1', '1', 'B'],
          ['B', 'B', 'B', 'B', 'B']]),
        ([['B', '1', 'E', '1', 'B'],
          ['B', '1', 'M', '1', 'B'],
          ['B', '1', '1', '1', 'B'],
          ['B', 'B', 'B', 'B', 'B']],
         [1, 2],
         [['B', '1', 'E', '1', 'B'],
          ['B', '1', 'X', '1', 'B'],
          ['B', '1', '1', '1', 'B'],
          ['B', 'B', 'B', 'B', 'B']])
    ),
    equal_func=is_matrix_equal,
    print_funcs=[print_matrix, None, print_matrix],
)
