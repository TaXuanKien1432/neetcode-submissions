class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        result = set()

        nums = sorted(nums) # O(nlogn)

        for pivot_index in range(len(nums)): # O(n)
            i = pivot_index + 1
            j = len(nums) - 1

            while i < j: # O(n)
                sum = nums[i] + nums[j]
                if sum == -1 * nums[pivot_index]:
                    result.add(tuple([nums[pivot_index], nums[i], nums[j]]))
                    i += 1
                elif sum < -1 * nums[pivot_index]:
                    i += 1
                elif sum > -1 * nums[pivot_index]:
                    j -= 1
            
        return [list(tup) for tup in result]
