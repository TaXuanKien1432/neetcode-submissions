class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # bruteforce: sort array then iterate to find global max sequence, O(nlogn)

        unique_nums = set(nums)
        global_max = 0
        
        for num in unique_nums:
            if num - 1 not in unique_nums:
                length = 1
                while (num+length) in unique_nums:
                    length += 1
                global_max = max(length, global_max)
        
        return global_max
                