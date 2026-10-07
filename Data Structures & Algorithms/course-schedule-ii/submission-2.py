class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visit, cycle = set(), set()
        adjList = {c: [] for c in range(numCourses)}
        for course, preq in prerequisites:
            adjList[course].append(preq)
        
        def dfs(course):
            if course in visit:
                return True
            if course in cycle:
                return False

            cycle.add(course)
            for preq in adjList[course]:
                if not dfs(preq):
                    return False
            # reach this if every dfs(preq) returns True, means that this course can be next added to res
            res.append(course)
            visit.add(course)
            cycle.remove(course)

            return True

        for course in adjList:
            if not dfs(course):
                return []
        return res