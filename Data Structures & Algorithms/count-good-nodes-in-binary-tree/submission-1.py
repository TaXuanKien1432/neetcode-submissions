# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, maxOnPath):
            if not node:
                return 0
            
            newMaxOnPath = max(node.val, maxOnPath)

            return (1 if node.val >= maxOnPath else 0) + dfs(node.left, newMaxOnPath) + dfs(node.right, newMaxOnPath)
        
        return dfs(root, root.val)