class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # bruteforce: sort array then iterate to find global max sequence, O(nlogn)

        unique_nums = set(nums)
        global_max = 0
        
        for num in unique_nums:
            if num - 1 not in unique_nums:
                current_max = 1
                next_num = num + 1
                while next_num in unique_nums:
                    current_max += 1
                    next_num += 1
                global_max = max(current_max, global_max)
        
        return global_max
                