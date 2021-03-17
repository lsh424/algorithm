import sys
sys.setrecursionlimit(10001)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_value(self.root, data)
        return

    def insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data[0] <= node.data[0]:
                node.left = self.insert_value(node.left, data)
            else:
                node.right = self.insert_value(node.right, data)
        return node


def solution(nodeinfo):
    i = 1
    tree = Tree()
    preorder_result = []
    postorder_result = []
    answer = []

    for node in nodeinfo:
        node.append(i)
        i += 1

    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    for node in nodeinfo:
        tree.insert(node)

    def order(node):
        preorder_result.append(node.data[-1])
        if not node.left == None: order(node.left)
        if not node.right == None: order(node.right)
        postorder_result.append(node.data[-1])

    order(tree.root)

    answer.append(preorder_result)
    answer.append(postorder_result)

    return answer