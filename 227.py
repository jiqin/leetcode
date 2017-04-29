class ValueNode(object):
    def __init__(self):
        self.v = None
        self.parent_node = None

    def level(self):
        return 0

    def parse(self, s, index):
        e = index
        assert ord('0') <= ord(s[e]) <= ord('9')

        while e < len(s):
            if ord('0') <= ord(s[e]) <= ord('9'):
                e += 1
            else:
                break
        self.v = int(s[index:e])
        return e

    def eval(self):
        return self.v

    def msg(self):
        return str(self.v)


class OpNode(object):
    def __init__(self):
        self.left_node = None
        self.right_node = None
        self.parent_node = None
        self.op = None

    def add_left_node(self, node):
        self.left_node = node
        node.parent_node = self

    def add_right_node(self, node):
        self.right_node = node
        node.parent_node = self

    def level(self):
        raise NotImplementedError()

    def parse(self, s, index):
        self.op = s[index]
        return index + 1

    def eval(self):
        raise NotImplementedError()

    def msg(self):
        m = '({}) {} ({})'.format(
            '.' if self.left_node is None else self.left_node.msg(),
            self.op,
            '.' if self.right_node is None else self.right_node.msg())
        return m


class OpAddNode(OpNode):
    def level(self):
        return 5

    def eval(self):
        return self.left_node.eval() + self.right_node.eval()


class OpSubNode(OpNode):
    def level(self):
        return 5

    def eval(self):
        return self.left_node.eval() - self.right_node.eval()


class OpMulNode(OpNode):
    def level(self):
        return 10

    def eval(self):
        return self.left_node.eval() * self.right_node.eval()


class OpDivNode(OpNode):
    def level(self):
        return 10

    def eval(self):
        return self.left_node.eval() / self.right_node.eval()


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        op_nodes = []
        pre_data_node = None
        index = 0
        while index < len(s):
            c = s[index]
            if c == ' ':
                index += 1
            elif c in '+-*/':
                assert pre_data_node is not None

                if c == '+':
                    op_node = OpAddNode()
                elif c == '-':
                    op_node = OpSubNode()
                elif c == '*':
                    op_node = OpMulNode()
                else:
                    op_node = OpDivNode()
                index = op_node.parse(s, index)

                if not op_nodes:
                    op_node.add_left_node(pre_data_node)
                elif op_nodes[-1].level() < op_node.level():
                    op_node.add_left_node(pre_data_node)
                    # op_nodes[-1].add_right_node(op_node)
                else:
                    op_nodes[-1].add_right_node(pre_data_node)
                    i = len(op_nodes) - 2
                    while i >= 0:
                        if op_nodes[i].level() >= op_node.level():
                            op_nodes[i].add_right_node(op_nodes[i+1])
                            i -= 1
                        else:
                            break
                    i += 1
                    op_node.add_left_node(op_nodes[i])
                    op_nodes = op_nodes[0:i]

                op_nodes.append(op_node)
                pre_data_node = None
            else:
                assert pre_data_node is None
                pre_data_node = ValueNode()
                index = pre_data_node.parse(s, index)

        op_nodes[-1].add_right_node(pre_data_node)
        for i in range(0, len(op_nodes) - 1):
            op_nodes[i].add_right_node(op_nodes[i+1])

        return op_nodes[0].eval()


print Solution().calculate('1 + 2 * 3 - 4 / 3 + 4 - 2')
