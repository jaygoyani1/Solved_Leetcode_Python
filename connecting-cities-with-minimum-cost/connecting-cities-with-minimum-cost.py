class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for x1,x2,cost in connections:
            adj[x1].append([cost,x2])
            adj[x2].append([cost,x1])
        
        heap = [(0,1)]
        heapq.heapify(heap)
        visited = set()
        total = 0
        
        while heap:
            cost,city = heapq.heappop(heap)
            if city not in visited:
                total+=cost
                visited.add(city)
                for ci,nei in adj[city]:
                    heapq.heappush(heap,[ci,nei])
        return total if len(visited) == n else -1        