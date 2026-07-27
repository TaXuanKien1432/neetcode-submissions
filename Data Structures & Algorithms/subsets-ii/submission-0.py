class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        curr = []
        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            # include this number only once
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()

            # exclude this number from subset completely
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res