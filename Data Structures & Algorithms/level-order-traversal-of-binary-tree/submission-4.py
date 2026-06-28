# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        if root:
            q = collections.deque()
            q.append(root)
            while q:
                currLayer = []
                for i in range(len(q)):
                    node = q.popleft()
                    currLayer.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                ans.append(currLayer)

        return ans