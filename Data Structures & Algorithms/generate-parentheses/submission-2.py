class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, openBracketsLeft, closeBracketsLeft):
            if closeBracketsLeft == 0:
                res.append(curr)
            
            # select open bracket for this position
            if openBracketsLeft >= 1:
                dfs(curr + "(", openBracketsLeft - 1, closeBracketsLeft)
            
            # select close bracket for this position
            if closeBracketsLeft > openBracketsLeft:
                dfs(curr + ")", openBracketsLeft, closeBracketsLeft - 1)

        dfs("", n, n)
        return res

