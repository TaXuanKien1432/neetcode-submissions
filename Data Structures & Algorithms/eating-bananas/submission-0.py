class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = float('-inf')
        for num in piles:
            ans = max(ans, num)
        
        left, right = 1, ans
        while left <= right:
            k = (left + right) // 2
            hour = h
            for num in piles:
                hour -= (num + k - 1) // k
                if hour < 0:
                    left = k + 1
                    break
            if hour >= 0:
                ans = min(ans, k)
                right = k - 1
        
        return ans
            



            