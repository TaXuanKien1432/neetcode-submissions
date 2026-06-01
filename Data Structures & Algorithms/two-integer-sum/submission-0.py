class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            other_number = target - nums[i]
            
            if other_number in counter:
                return [counter[other_number], i]
            
            if nums[i] not in counter:
                counter[nums[i]] = i
        return []