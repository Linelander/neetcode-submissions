"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        seen = defaultdict(Node)

        def dfs(node: Optional['Node'], clone):
            # mark current node as seen
            seen[clone.val] = clone
            # add it to clone... somehow
            print(node.val)

            for i in range(len(node.neighbors)):
                # filter out seen nodes
                if node.neighbors[i].val not in seen:
                    # create the valid neighbor in clone in the right spot
                    # iterate to that spot in both the original and clone
                    clone.neighbors.append(Node(node.neighbors[i].val))
                    dfs(node.neighbors[i], clone.neighbors[len(clone.neighbors) - 1])
                else: # cycle detector and handler
                    clone.neighbors.append(seen[node.neighbors[i].val])

        clone = Node(node.val)
        dfs(node, clone)
        return clone