class Solution1(object):
    def isNumber(self, s):
        """
        Valid number:
        [+-]?[0-9]+[.]?[0-9]+(e[+-]?[0-9]+)
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0:
            return False

        index = 0
        if s[0] in '+-':
            index += 1

        return self.before_e_and_point(s, index)

    def before_e_and_point(self, s, index):
        if index == len(s):
            return False

        n, index = self.scan_digit(s, index)
        if index == len(s):
            return n > 0

        if s[index] == '.':
            return self.before_e_after_point(s, index + 1, n)
        elif s[index] in 'eE':
            if n == 0:
                return False
            return self.after_e(s, index + 1)
        else:
            return False

    def before_e_after_point(self, s, index, n):
        n1, index = self.scan_digit(s, index)
        if n == 0 and n1 == 0:
            return False

        if index == len(s):
            return True

        if s[index] in 'eE':
            return self.after_e(s, index + 1)

        return False

    def after_e(self, s, index):
        if index == len(s):
            return False

        if s[index] in '-+':
            index += 1

        n, index = self.scan_digit(s, index)

        if index != len(s):
            return False
        if n == 0:
            return False
        return True

    def scan_digit(self, s, index):
        n = 0
        while index < len(s) and s[index].isdigit():
            index += 1
            n += 1
        return n, index


class Solution(object):
    def isNumber(self, s):
        status_transfer = {
            0: [6, 7, -1, 1, 0],
            1: [-1, 7, 2, 1, 5],
            2: [3, -1, -1, 4, -1],
            3: [-1, -1, -1, 4, -1],
            4: [-1, -1, -1, 4, 5],
            5: [-1, -1, -1, -1, 5],
            6: [-1, 7, -1, 1, -1],
            7: [-1, -1, -1, 8, -1],
            8: [-1, -1, 2, 8, 5],
        }

        status = 0
        for c in s:
            cond = self.get_condition(c)
            if cond is None:
                return False
            status = status_transfer[status][cond]
            if status < 0:
                return False

        return status in [1, 4, 5, 8]

    def get_condition(self, c):
        if c in '+-':
            return 0
        elif c in '.':
            return 1
        elif c in 'eE':
            return 2
        elif c in '0123456789':
            return 3
        elif c in ' ':
            return 4
        else:
            return None


for args, result in (
        ('1 ', True),
        (' 1.0', True),
        ('.10', True),
        ('10.', True),
        ('.', False),
        ('e', False),
        ('1.e', False),
        ('01.02', True),
        ('-01.02', True),
        ('-01.02e1', True),
        ('-01.02e52', True),
        ('-01.02e-52', True),
        ('-01.0.2', False),
        ('-01.02e0.1', False),
):
    r = Solution().isNumber(args)
    print '{}: {}, {}'.format('Passed' if r == result else '>>> Fail', args, r)
