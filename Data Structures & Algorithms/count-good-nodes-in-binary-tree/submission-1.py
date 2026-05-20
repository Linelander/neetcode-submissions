# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodDFS(root, float('-inf'))
        
        
    def goodDFS(self, root: TreeNode, max) -> int:
        if not root: return 0
        good = 0
        if root.val >= max:
            max = root.val
            good = 1
        return good + self.goodDFS(root.left, max) + self.goodDFS(root.right, max)