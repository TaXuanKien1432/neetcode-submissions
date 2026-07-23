class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, sum):
            if sum == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or sum > target:
                return
            
            # omit current number
            dfs(i + 1, curr, sum)

            # include current number
            curr.append(nums[i])
            dfs(i, curr, sum + nums[i])
            curr.pop()

        dfs(0, [], 0)
        return res