class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prqMap = { i:[] for i in range(numCourses)}
        for crs, prq in prerequisites:
            prqMap[crs].append(prq)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if prqMap[crs] == []:
                return True
            
            visited.add(crs)
            for prq in prqMap[crs]:
                if not dfs(prq):
                    return False
            visited.remove(crs)
            prqMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

