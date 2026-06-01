class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1
        
        for char in t:
            if char not in map:
                return False
            else:
                map[char] -= 1
        
        for char in map.keys():
            if map[char] != 0:
                return False
        
        return True