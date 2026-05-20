# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        thisres = self.treeComp(root, subRoot)
        leftres = self.isSubtree(root.left, subRoot)
        rightres = self.isSubtree(root.right, subRoot)
        return (thisres or leftres or rightres) # only need one



        

    def treeComp(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True 
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False

        lres = self.treeComp(root1.left, root2.left)
        rres = self.treeComp(root1.right, root2.right)

        return lres and rres