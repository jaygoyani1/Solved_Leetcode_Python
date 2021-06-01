class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = collections.defaultdict(list)
        
        for i,j in edges:
            dic[i].append(j)
            dic[j].append(i)
        
        visited = set()
        
        def bfs(i):
            queue = [i]
            visited.add(i)
            while queue:
                n= len(queue)
                for _ in range(n):
                    node = queue.pop(0)
                    for n in dic[node]:
                        if n not in visited:
                            queue.append(n)
                            visited.add(n)
        
        count = 0
        for x in range(n):
            if x not in visited:
                bfs(x)
                count+=1
        return count
        