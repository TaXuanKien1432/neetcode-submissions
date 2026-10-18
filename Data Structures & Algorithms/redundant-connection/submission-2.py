class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            res = node
            while res != parent[node]:
                parent[node] = parent[parent[node]]
                res = parent[node]
            return res

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return False
            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True

        for node1, node2 in edges:
            if not union(node1 - 1, node2 - 1):
                return [node1, node2]
