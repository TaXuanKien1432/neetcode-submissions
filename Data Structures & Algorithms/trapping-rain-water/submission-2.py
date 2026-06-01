class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute force: O(n^2) time, O(1) space. Iterate through the array, for each number, iterate its left and its right subarray to find highest bar on its left and right
        # Optimal solution: O(n) time, O(1) space.
        # Idea: suppose we know the highest bar on the left, if we know there exist
        # one bar on the right which is higher than highest bar on the left
        # then the height of the bar we are considering can be calculated
        # using highest bar on the left. similarly on the right. so use two pointers

        if len(height) <= 2:
            return 0

        ans = 0
        max_left, max_right = height[0], height[-1]
        l, r = 1, len(height) -2

        while l <= r:
            if max_left <= max_right:
                water = max_left - height[l]
                if water < 0:
                    water = 0
                ans += water

                max_left = max(max_left, height[l])
                l += 1
            else:
                water = max_right - height[r]
                if water < 0:
                    water = 0
                ans += water

                max_right = max(max_right, height[r])
                r -= 1

        return ans


