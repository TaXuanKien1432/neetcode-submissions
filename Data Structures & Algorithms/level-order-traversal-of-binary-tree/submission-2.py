# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        if root:
            q = deque()
            q.append(root)
            currLayerCount = 1
            nextLayerCount = 0
            currLayer = []
            while len(q) > 0:
                node = q.popleft()
                currLayerCount -= 1
                currLayer.append(node.val)
                if node.left:
                    q.append(node.left)
                    nextLayerCount += 1
                if node.right:
                    q.append(node.right)
                    nextLayerCount += 1
                if currLayerCount == 0:
                    ans.append(currLayer)
                    currLayer = []
                    currLayerCount = nextLayerCount
                    nextLayerCount = 0

        return ans