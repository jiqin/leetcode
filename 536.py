# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s == '':
            return None
        trees = []
        ns = ''
        for c in s:
            if c == '(':
                if len(ns) > 0:
                    t = TreeNode(int(ns))
                    ns = ''
                    if len(trees) > 0:
                        self._append_to_node(trees[-1], t)
                    trees.append(t)
                else:
                    pass
            elif c == ')':
                if len(ns) > 0:
                    t = TreeNode(int(ns))
                    ns = ''
                    self._append_to_node(trees[-1], t)
                else:
                    trees.pop(-1)
            else:
                ns += c
        if len(ns) == 0:
            assert len(trees) == 1
        else:
            assert len(trees) == 0
            trees.append(TreeNode(int(ns)))
        return trees[0]

    def _append_to_node(self, parent, child):
        if parent.left is None:
            parent.left = child
        else:
            assert parent.right is None
            parent.right = child


from my_algorithm.common_test import run_test_cases


t = TreeNode(4)
t.left = TreeNode(2)
t.left.left = TreeNode(3)
t.left.right = TreeNode(1)
t.right = TreeNode(6)
t.right.left = TreeNode(5)


def equal_func(t1, t2):
    if t1 is None:
        return t2 is None
    if t2 is None:
        return False
    if t1.val != t2.val:
        return False
    r1 = equal_func(t1.left, t2.left)
    r2 = equal_func(t1.right, t2.right)
    return r1 and r2


run_test_cases(
    Solution().str2tree,
    (
        ('4(2(3)(1))(6(5))', t),
        ('4', TreeNode(4))
    ),
    equal_func=equal_func,
)
