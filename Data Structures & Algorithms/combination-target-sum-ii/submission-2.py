class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, curr, sum):
            if sum == target:
                res.append(curr.copy())
                return
            if sum > target or i >= len(candidates):
                return
            
            # include this number
            curr.append(candidates[i])
            dfs(i + 1, curr, sum + candidates[i])
            curr.pop()

            # not include this number at anytime
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, curr, sum)

        dfs(0, [], 0)
        return res