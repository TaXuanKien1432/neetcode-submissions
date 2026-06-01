class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = dict()
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
            if map[i] >= 2:
                return True
        return False