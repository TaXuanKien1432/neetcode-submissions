class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sum = [0]
        curr = []
        def dfs(i):
            if sum[0] > target:
                return
            if sum[0] == target:
                res.append(curr.copy())
                return
            if i >= len(nums):
                return
            
            # omit current number
            dfs(i + 1)

            # include current number
            sum[0] += nums[i]
            curr.append(nums[i])
            dfs(i)
            sum[0] -= nums[i]
            curr.pop()

        dfs(0)
        return res