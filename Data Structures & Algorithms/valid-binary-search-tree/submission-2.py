# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node): # return [bool, minValue, maxValue]
            if not node:
                return [True, 1001, -1001]
            
            left = dfs(node.left)
            if not left[0]:
                return [False, 0, 0]
            right = dfs(node.right)
            if not right[0]:
                return [False, 0, 0]
            
            if left[2] < node.val and node.val < right[1]:
                return [True, left[1] if left[1] != 1001 else node.val, right[2] if right[2] != -1001 else node.val]
            
            return [False, 0, 0]
        
        return dfs(root)[0]
