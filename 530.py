# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, _, ret = self._find_tree_node_min_max_ret(root)
        return ret

    def _find_tree_node_min_max_ret(self, root):
        if root is None:
            return None, None, None

        lmin, lmax, lret = self._find_tree_node_min_max_ret(root.left)
        rmin, rmax, rret = self._find_tree_node_min_max_ret(root.right)
        ret = None
        if lmax:
            ret = min(ret, root.val - lmax) if ret else (root.val - lmax)
        if rmin:
            ret = min(ret, rmin - root.val) if ret else (rmin - root.val)
        if lret:
            ret = min(ret, lret) if ret else lret
        if rret:
            ret = min(ret, rret) if ret else rret

        if lmin is None:
            lmin = root.val
        if rmax is None:
            rmax = root.val
        return lmin, rmax, ret


def to_tree_node(values):
    root = TreeNode(values[0])
    values.pop(0)
    stacks = [root]
    while stacks:
        node = stacks.pop(0)
        if values:
            v = values.pop(0)
            if v:
                node.left = TreeNode(v)
                stacks.append(node.left)
        if values:
            v = values.pop(0)
            if v:
                node.right = TreeNode(v)
                stacks.append(node.right)
    return root


def print_tree_nodes(root):
    nodes = [root]
    while nodes:
        if not any(map(lambda n: n is not None, nodes)):
            break
        children = []
        s = ''
        for node in nodes:
            if node:
                s += str(node.val) + ' '
                children.append(node.left)
                children.append(node.right)
            else:
                s += '. '
                children.append(None)
                children.append(None)
        print s
        nodes = children


def test():
    for values, result in (
        # ([1, None, 3, 2], 1),
        # ([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 20], 1),
        # ([5, 4, 7], 1),
        ([1, None, 5, 3], 2),
    ):
        root = to_tree_node(values)
        ret = Solution().getMinimumDifference(root)
        print_tree_nodes(root)
        print ret


test()
