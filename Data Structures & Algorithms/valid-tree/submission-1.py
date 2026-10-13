class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        
        adjList = {c: [] for c in range(n)}
        for A, B in edges:
            adjList[A].append(B)
            adjList[B].append(A)
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbour in adjList[node]:
                if neighbour != prev and not dfs(neighbour, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return n == len(visited)
                