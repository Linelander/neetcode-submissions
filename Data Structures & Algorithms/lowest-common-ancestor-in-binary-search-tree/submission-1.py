# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return None
        if root.val == p.val: return p
        if root.val == q.val: return q        

        lres = None
        rres = None

        lres = self.lowestCommonAncestor(root.left, p, q)
        rres = self.lowestCommonAncestor(root.right, p, q)

        if lres and rres: return root
        return lres or rres

        # "ancestor is descendent of itself" is implicitly handled by the guarantee
        # that the other value we're looking for exists in the tree somewhere.