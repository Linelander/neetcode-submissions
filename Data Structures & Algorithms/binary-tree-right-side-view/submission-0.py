# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        self.getLevels(root, levels, 0)
        rightside = []
        # print(levels)
        for lvl in levels: rightside.append(lvl[len(lvl) - 1])
        return rightside

    def getLevels(self, root: Optional[TreeNode], levels, depth):
        if not root: return
        if depth == len(levels): levels.append([])
        levels[depth].append(root.val)
        self.getLevels(root.left, levels, depth + 1)
        self.getLevels(root.right, levels, depth + 1)
