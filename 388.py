class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        result = 0
        path_list = []
        level = -1
        length = 0
        is_file = False
        for c in input:
            if c not in ['\n', '\t']:
                if level >= 0:
                    assert level <= len(path_list)
                    path_list = path_list[0:level]
                    level = -1
                length += 1
                if c == '.':
                    is_file = True
            elif c == '\n':
                if is_file:
                    cur_result = sum(path_list) + length + len(path_list)
                    if cur_result > result:
                        result = cur_result
                else:
                    path_list.append(length)
                length = 0
                if level < 0:
                    level = 0
                is_file = False
            elif c == '\t':
                if level < 0:
                    level = 0
                level += 1
        if is_file:
            cur_result = sum(path_list) + length + len(path_list)
            if cur_result > result:
                result = cur_result
        return result


for s in [
    "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
]:
    print Solution().lengthLongestPath(s)
