class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        black_map = {}
        for row in range(len(picture)):
            columns = []
            for column in range(len(picture[0])):
                if picture[row][column] == 'B':
                    columns.append(column)
            for column in columns:
                black_map.setdefault(row, {}).setdefault(column, [0, 0])[0] = len(columns)

        for column in range(len(picture[0])):
            rows = []
            for row in range(len(picture)):
                if picture[row][column] == 'B':
                    rows.append(row)
            for row in rows:
                black_map.setdefault(row, {}).setdefault(column, [0, 0])[1] = rows

        row_equal_map = {}
        ret = 0
        for row, v1 in black_map.iteritems():
            for column, v in v1.iteritems():
                if v[0] == N and len(v[1]) == N:
                    is_all_equal = True
                    for row1 in v[1]:
                        a = min(row, row1)
                        b = max(row, row1)
                        key = '{}_{}'.format(a, b)
                        if key not in row_equal_map:
                            row_equal_map[key] = (picture[row] == picture[row1])
                        if not row_equal_map[key]:
                            is_all_equal = False
                            break
                    if is_all_equal:
                        ret += 1
        return ret


from my_algorithm.common_test import run_test_cases, print_matrix

run_test_cases(
    Solution().findBlackPixel,
    (
        (
            [['W', 'B', 'W', 'B', 'B', 'W'],
             ['W', 'B', 'W', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'B', 'W'],
             ['W', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'W', 'W', 'B', 'B', 'W']],
            3,
            0
        ),
        (
            [['W', 'B', 'W', 'B', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'B', 'W'],
             ['W', 'W', 'B', 'W', 'B', 'W']],
            3,
            6
        ),
        (
            [['W', 'B', 'W', 'B', 'W', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'W'],
             ['W', 'B', 'W', 'B', 'B', 'W'],
             ['W', 'W', 'B', 'W', 'B', 'W']],
            2,
            0
        ),
    ),
    print_funcs=(print_matrix, None, None),
)
