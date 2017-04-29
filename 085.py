class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        new_matrix = self.generate_new_matrix(matrix)
        # print new_matrix
        values = []
        max_v = 0
        for i in range(len(new_matrix)):
            vs = []
            for j in range(len(new_matrix[i])):
                vs.append(self.get_max_rectangle(new_matrix, i, j))
            values.append(vs)
            max_v = max(max_v, max(vs))

        # print values
        return max_v

    def generate_new_matrix(self, matrix):
        new_matrix = []
        for m in matrix:
            m1 = map(int, m)
            for i in range(len(m1) - 2, -1, -1):
                if m1[i] == 1 and m1[i + 1] != 0:
                    m1[i] = m1[i + 1] + 1
            new_matrix.append(m1)
        return new_matrix

    def get_max_rectangle(self, matrix, i, j):
        max_l = matrix[i][j]
        r = 0
        for i1 in range(i, len(matrix)):
            max_l = min(max_l, matrix[i1][j])
            if max_l == 0:
                break

            r1 = (i1 - i + 1) * max_l
            r = max(r, r1)
        return r


def test():
    for matrix in (
            (
                    '10100',
                    '10111',
                    '11111',
                    '10010'
            ),
            (
                    '11100110',
                    '11001100',
                    '11111111',
                    '10000000',
                    '11000100',
                    '01000010',
            ),
    ):
        print Solution().maximalRectangle(matrix)


test()
