class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow1, slow2 = 0, slow
        while True:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
            if slow1 == slow2:
                return slow1