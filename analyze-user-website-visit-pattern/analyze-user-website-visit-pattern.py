class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        users = collections.defaultdict(list)
        
        for user,time,site in sorted(zip(username,timestamp,website), key = lambda x:x[1]):
            users[user].append(site)
            
        count = collections.defaultdict(int)
        maximum = 0
        result = tuple()
        
        for user in users:
            combo = combinations(users[user],3)
            for i in set(combo):
                count[i] += 1
                if count[i] > maximum:
                    maximum = count[i]
                    result = i
                elif count[i] == maximum:
                    if i < result:
                        result = i
        return result
                
        