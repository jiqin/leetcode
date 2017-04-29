import copy


class Solution(object):
    def largestRectangleArea(self, heights):
        if not heights:
            return 0

        heights = copy.copy(list(heights))

        r = 0
        height_index = [0]
        # print 0, r, heights, height_index

        for i, h in enumerate(heights):
            h1 = heights[height_index[-1]]
            if h1 == h:
                continue
            elif h1 < h:
                height_index.append(i)
            else:
                pre_index = height_index[-1]
                while height_index:
                    i1 = height_index[-1]
                    h1 = heights[i1]
                    if h1 > h:
                        r = max(r, h1 * (i - i1))
                        height_index.pop(-1)
                    else:
                        if h1 < h:
                            heights[pre_index] = h
                            height_index.append(pre_index)
                        break
                    pre_index = i1

                if not height_index:
                    heights[0] = h
                    height_index.append(0)
            # print i, r, heights, height_index

        for i in height_index:
            r = max(r, heights[i] * (len(heights) - i))

        return r


def test():
    for heights in (
            (4,2,0,3,2,5),
            (2, 1, 2),
            (2,1,5,6,2,3),
            (1, 2, 3, 4, 5, 6, 7),
            (7, 6, 5, 4, 3, 2, 1),
            (7, 6, 5, 4, 3, 2, 1, 0),
            (1, 2, 3, 4, 2, 6, 5),
            list(range(10000)),
            list(range(10000, 0, -1)),
            list(range(10000)) + list(range(10000, 0, -1)),
            list(range(10000, 0, -1)) + list(range(10000)),
    ):
        print Solution().largestRectangleArea(heights)


test()
