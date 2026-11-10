class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        graph = collections.defaultdict(list)
        for source, destination in tickets:
            graph[source].append(destination)
        
        res = []
        
        def dfs(source):
            while graph[source]:
                nextDestination = graph[source].pop()
                dfs(nextDestination)
            res.append(source)
        
        dfs("JFK")
        return res[::-1]