# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        count = 0

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
                continue
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            root = node.right
            
