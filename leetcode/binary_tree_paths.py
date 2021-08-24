# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        stack = [(root, str(root.val))]
        visit = []

        while stack:
            node, string = stack.pop()
            visit.append(node)

            if node.left == None and node.right == None:
                answer.append(string)
                continue

            if node.left != None and node.left not in visit:
                stack.append((node.left, string + "->" + str(node.left.val)))

            if node.right != None and node.right not in visit:
                stack.append((node.right, string + "->" + str(node.right.val)))

        return answer