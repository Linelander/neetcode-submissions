# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal with global counter
        self.counter = 0
        return self.inorder(root, k)

    def inorder(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return

        left = self.inorder(root.left, k)
        if left: return left

        self.counter += 1
        if self.counter == k:
            return root.val

        return self.inorder(root.right, k)