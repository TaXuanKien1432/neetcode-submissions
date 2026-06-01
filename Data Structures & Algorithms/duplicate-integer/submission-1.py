class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1
            if map[i] >= 2:
                return True
        return False