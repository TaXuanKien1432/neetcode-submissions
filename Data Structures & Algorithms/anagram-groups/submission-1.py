class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list) # maps a counter to a list of anagrams
        for s in strs:
            counter = [0] * 26

            for char in s:
                counter[ord(char) - ord('a')] += 1
            
            anagrams_dict[tuple(counter)].append(s)
        return list(anagrams_dict.values())