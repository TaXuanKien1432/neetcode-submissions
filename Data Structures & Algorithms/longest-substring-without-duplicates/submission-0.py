class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        store = set()
        ans = 1

        l, r = 0, 0
        while r < len(s):
            if s[r] not in store:
                length = r + 1 - l
                ans = max(ans, length)
                store.add(s[r])
                r += 1
            else:
                store.remove(s[l])
                l += 1
        
        return ans


        