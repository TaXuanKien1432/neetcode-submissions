class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque() # stores index
        res = []
        l, r = 0, 0

        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            while dq and dq[0] < l:
                dq.popleft()
            dq.append(r)
            
            if r + 1 - l == k:
                res.append(nums[dq[0]])
                l += 1
            r += 1
        
        return res