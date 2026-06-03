class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                ans = min(ans, nums[mid])
                right = mid - 1
        return ans