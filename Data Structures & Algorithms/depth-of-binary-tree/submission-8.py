# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dive(root, 0)

    def dive(self, root: Optional[TreeNode], n) -> int:
        if (not root.left and not root.right):
            return n+1
        
        l, r = 0, 0
        if (root.left):
            r = self.dive(root.left, n+1)
        if (root.right):
            l = self.dive(root.right, n+1)
        return max(l, r)
        