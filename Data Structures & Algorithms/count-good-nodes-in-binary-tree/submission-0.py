# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodcount = 0
        self.goodDFS(root, float('-inf'))
        return self.goodcount
        
    def goodDFS(self, root: TreeNode, max):
        if not root: return
        if root.val >= max:
            max = root.val
            self.goodcount += 1
        self.goodDFS(root.left, max)
        self.goodDFS(root.right, max)