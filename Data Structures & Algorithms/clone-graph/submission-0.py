"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeStore = {} # node.val : node
        def dfs(node):
            if not node:
                return None
            
            if node.val not in nodeStore:
                copyNode = Node(node.val)
                nodeStore[copyNode.val] = copyNode
            else:
                copyNode = nodeStore[node.val]
            
            if node.neighbors:
                if not copyNode.neighbors:
                    copyNode.neighbors = []
                for neighbor in node.neighbors:
                    if neighbor:
                        if neighbor.val in nodeStore:
                            copyNode.neighbors.append(nodeStore[neighbor.val])
                        else:
                            copyNode.neighbors.append(dfs(neighbor))
            
            return copyNode

        return dfs(node)
                    
