# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.bfs(root, 0, result)
        return result
    
    def bfs(self, root, depth, result):
        if not root: return

        if depth == len(result):
            result.append([])

        result[depth].append(root.val)

        self.bfs(root.left, depth + 1, result)
        self.bfs(root.right, depth + 1, result)