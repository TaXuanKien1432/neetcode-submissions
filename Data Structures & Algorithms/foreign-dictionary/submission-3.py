class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        resList = []
        adj = { c:set() for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} # c : bool
        # c not in visit -> not visited & not in path
        # c : True -> c is visited & not in path
        # c : False -> c is visited & in path
            
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = False
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            resList.append(c)
            visit[c] = True
            return True
        
        for c in adj:
            if not dfs(c):
                return ""
        
        return "".join(resList[::-1])

            
