# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # trying BFS
        result = []
        q = deque([root])

        while q:
            level = []
            # things in q when while starts is the entire level
            lvlLen = len(q)

            for _ in range(lvlLen):
                curr = q.popleft()
                if curr: 
                    level.append(curr.val)
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)
            if level:
                result.append(level)

        return result