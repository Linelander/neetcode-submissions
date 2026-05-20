# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        self.inorder(root, result)
        return all(result[i] < result[i+1] for i in range(len(result) - 1))


    def inorder(self, root: Optional[TreeNode], result):
        if not root: return
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)