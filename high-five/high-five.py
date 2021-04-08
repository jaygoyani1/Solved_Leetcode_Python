class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        dic ={}
        for item in items:
            if item[0] in dic:
                dic[item[0]].append(item[1])
            else:
                dic[item[0]] = [item[1]]
        ans = []
        
        def sort(list):
            list = sorted(list,reverse=True)
            return int(sum(list[0:5])/5)
        
        for item in dic:
            ans.append([item,sort(dic[item])])
        return sorted(ans)
        
            
        