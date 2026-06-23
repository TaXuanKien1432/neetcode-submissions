# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxDiameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            diameter = self.height(root.left) + self.height(root.right)
            self.maxDiameter = max(diameter, self.maxDiameter)
            self.diameterOfBinaryTree(root.left)
            self.diameterOfBinaryTree(root.right)
            return self.maxDiameter

    def height(self, root):
        if root == None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))