class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        counter = {}
        l = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            cur_length = r + 1 - l
            if cur_length - max(counter.values()) <= k:
                ans = max(ans, cur_length)
            else:
                counter[s[l]] -= 1
                l += 1
        return ans
            
