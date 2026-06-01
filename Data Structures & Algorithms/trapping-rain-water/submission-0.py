class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute force: O(n^2) time, O(1) space. Iterate through the array, for each number, iterate its left and its right subarray to find highest bar on its left and right
        ans = 0
        
        left = [0] * len(height)
        right = [0] * len(height)

        highest = 0
        for i in range(len(height)):
            left[i] = highest
            highest = max(highest, height[i])

        highest = 0
        for i in range(len(height) - 1, -1, -1):
            right[i] = highest
            highest = max(highest, height[i])

        for i in range(len(height)):
            water = min(left[i], right[i]) - height[i]
            if water < 0:
                water = 0
            ans += water

        return ans