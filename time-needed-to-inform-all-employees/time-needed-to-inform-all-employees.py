class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dic = collections.defaultdict(list)
        
        for i,person in enumerate(manager):
            dic[person].append(i)
        
        total = 0
        
        q = []
        q.append([headID,0])
        
        total = 0
        
        while q:
            person, time = q.pop(0)
            
            passtime = informTime[person]
            if person in dic:
                for i in dic[person]:
                    q.append([i,time+passtime])
            else:
                total = max(total, time)
        return total
            
            