class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = [] # stores tuple of number and index
        for i, num in enumerate(temperatures):
            while st and num > st[-1][0]:
                res[st[-1][1]] = i - st[-1][1]
                st.pop()
            st.append((num, i))
        return res
            