class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        number_mapping = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'Hundred',
            1000: 'Thousand',
            1000000: 'Million',
            1000000000: 'Billion',
        }

        def _three_number(_n):
            assert 0 < _n < 1000
            _ws = []
            if _n >= 100:
                a = _n / 100
                _n %= 100
                _ws.append(number_mapping[a])
                _ws.append(number_mapping[100])
            if _n >= 20:
                a = _n / 10 * 10
                _n %= 10
                _ws.append(number_mapping[a])
            if _n > 0:
                _ws.append(number_mapping[_n])
            return _ws

        if num == 0:
            return number_mapping[0]

        ws = []
        splits = [1000000000, 1000000, 1000]
        for split in splits:
            if num >= split:
                n = num / split
                num %= split
                ws.extend(_three_number(n))
                ws.append(number_mapping[split])
        if num > 0:
            ws.extend(_three_number(num))
        return ' '.join(ws)


for n, s in (
        (1000, "One Thousand"),
        (100, "One Hundred"),
        (123, "One Hundred Twenty Three"),
        (12345, "Twelve Thousand Three Hundred Forty Five"),
        (1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
        (1234567890, "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety"),
):
    r = Solution().numberToWords(n)
    if r != s:
        print '>>> Failed:', n
        print s
        print r
    else:
        print 'Passed'
