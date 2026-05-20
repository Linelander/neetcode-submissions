# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    biggest = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # for each node
        # get the depth of its longest paths down
        # on each side
        # then add them up

        left = self.getDepth(root.left, 0)
        right = self.getDepth(root.right, 0)

        self.biggest = max(self.biggest, left + right)

        if root.left: self.diameterOfBinaryTree(root.left)
        if root.right: self.diameterOfBinaryTree(root.right)

        return self.biggest



    def getDepth(self, root: Optional[TreeNode], depth: int) -> int:
        if not root: return depth

        print(depth)

        left = self.getDepth(root.left, depth + 1)
        right = self.getDepth(root.right, depth + 1)
        return max(left, right)