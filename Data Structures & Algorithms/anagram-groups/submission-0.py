class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # maps a counter to a list of anagrams
        for s in strs:
            counter = [0] * 26

            for char in s:
                counter[ord(char) - ord('a')] += 1
            
            result[tuple(counter)].append(s)
        return list(result.values())