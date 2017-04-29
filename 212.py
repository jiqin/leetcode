class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        word_map = {}
        for word in words:
            for i in range(len(word)):
                word_map[word[0:i+1]] = 0
        for word in words:
            word_map[word] = 1
        # print word_map

        results = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                tmp_word = ''
                history_pos = []
                heap = [(i, j, 0)]

                while heap:
                    x, y, l = heap.pop()
                    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                        continue
                    assert len(history_pos) >= l
                    history_pos = history_pos[0:l]
                    if (x, y) in history_pos:
                        continue
                    assert len(tmp_word) >= l
                    tmp_word = tmp_word[0:l] + board[x][y]
                    history_pos.append((x, y))
                    # print x, y, tmp_word, heap, history_pos
                    value = word_map.get(tmp_word)
                    if value is None:
                        continue
                    if value == 1:
                        results.append(tmp_word)

                    heap.append((x - 1, y, l + 1))
                    heap.append((x + 1, y, l + 1))
                    heap.append((x, y - 1, l + 1))
                    heap.append((x, y + 1, l + 1))

        return list(set(results))


for b, w in (
        # ([
        #      ['o', 'a', 'a', 'n'],
        #      ['e', 't', 'a', 'e'],
        #      ['i', 'h', 'k', 'r'],
        #      ['i', 'f', 'l', 'v']
        #  ],
        #  ["oath", "pea", "eat", "rain"]),
        # (['ab', 'cd'], ['acdb']),
        # (["ab","cd"],  ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]),
        (["abc","aed","afg"], ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]),
):
    print Solution().findWords(b, w)
