class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
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
                black_map.setdefault(row, {}).setdefault(column, [0, 0])[1] = len(rows)

        ret = 0
        for row, v1 in black_map.iteritems():
            for column, v in v1.iteritems():
                if v[0] == 1 and v[1] == 1:
                    ret += 1
        return ret


from my_algorithm.common_test import run_test_cases, print_matrix

run_test_cases(
    Solution().findLonelyPixel,
    (
        (
            [['W', 'W', 'B'],
             ['W', 'B', 'W'],
             ['B', 'W', 'W']],
            3,
        ),
        (
            [['W', 'W', 'B'],
             ['W', 'B', 'W'],
             ['B', 'W', 'B'],
             ['W', 'W', 'B']],
            1,
        ),
    ),
    print_funcs=[print_matrix, None],
)
