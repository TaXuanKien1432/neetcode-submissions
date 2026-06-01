class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        for c in s:
            if c in map_s:
                map_s[c] += 1
            else:
                map_s[c] = 1

        for c in t:
            if c in map_t:
                map_t[c] += 1
            else:
                map_t[c] = 1

        for c in map_s.keys():
            if map_s[c] != map_t.get(c, 0):
                return False

        for c in map_t.keys():
            if map_t[c] != map_s.get(c, 0):
                return False

        return True