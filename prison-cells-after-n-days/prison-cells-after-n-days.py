class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next(temp):
            arr = [0]*8
            for i in range(1,len(arr)-1):
                if temp[i-1] == temp[i+1]:
                    arr[i] = 1
            return arr
        dic = {}
        
        for i in range(n):
            currcell = str(cells)
            if currcell not in dic:
                dic[currcell] = i
                cells = next(cells)
            else:
                total = i - dic[currcell]
                return self.prisonAfterNDays(cells,(n-i)%total)
        return cells
            
            
        
        
        
        