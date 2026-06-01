class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_counter = 0
        non_zero_product = 1
        result = []
        for i in nums:
            if i == 0:
                zero_counter += 1
            if i != 0:
                non_zero_product *= i
        
        if zero_counter >= 2:
            return [0] * len(nums)
        elif zero_counter == 1:
            for i in nums:
                if i == 0:
                    result.append(non_zero_product)
                else:
                    result.append(0)
        else:
            for i in nums:
                result.append(int(non_zero_product / i))
        
        return result
