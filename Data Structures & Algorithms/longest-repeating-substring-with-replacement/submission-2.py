class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        counter = {s[0]: 1}
        l, r = 0, 0

        def get_most_frequent():
            most_frequent = 0
            for s, f in counter.items():
                most_frequent = max(most_frequent, f)
            return most_frequent

        while r < len(s):
            cur_length = r + 1 - l
            if cur_length - get_most_frequent() <= k:
                ans = max(ans, cur_length)
                r += 1
                if r < len(s):
                    counter[s[r]] = 1 + counter.get(s[r], 0)
            else:
                counter[s[l]] -= 1
                l += 1
        
        return ans
            
