class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        users = collections.defaultdict(list)
        
        for user,time,site in sorted(zip(username,timestamp,website), key = lambda x:(x[0],x[1])):
            users[user].append(site)
        
        permutations = Counter()
        
        for user,site in users.items():
            permutations.update(Counter(set(combinations(site,3))))
        
        return max(sorted(permutations), key = permutations.get)