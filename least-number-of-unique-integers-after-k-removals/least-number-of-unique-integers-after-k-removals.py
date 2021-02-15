class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        diclist = []
        count = 0
        for i in range(len(arr)):
            if arr[i] in dic:
                dic[arr[i]] += 1
            else:
                dic[arr[i]] = 1
        
        for i in dic:
            diclist.append([dic[i],i])
        diclist.sort()
        n = len(diclist)
        for i in range(n):
            if (diclist[i][0] <= k):
                k -= diclist[i][0]
                count+=1
            else:
                return n-count
        return n-count
        
        