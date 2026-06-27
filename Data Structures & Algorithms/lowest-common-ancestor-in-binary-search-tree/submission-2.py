# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        a, b = p, q
        if p.val > q.val:
            a, b = b, a
        
        if root:
            if root.val > a.val and root.val < b.val:
                return root
            elif root.val < a.val:
                return self.lowestCommonAncestor(root.right, a, b)
            elif root.val > b.val:
                return self.lowestCommonAncestor(root.left, a, b)
            elif root.val == a.val:
                return a
            elif root.val == b.val:
                return b