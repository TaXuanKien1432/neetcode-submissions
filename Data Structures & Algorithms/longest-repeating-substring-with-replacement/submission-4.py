class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        counter = {}
        l = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            while (r + 1 - l) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            ans = max(ans, r + 1 - l)
        return ans
            
