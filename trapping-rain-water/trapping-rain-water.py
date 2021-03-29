class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r = 0,len(height)-1
        maxl,maxr = height[l], height[r]
        total = 0
        while l<r:
            maxl = max(maxl,height[l])
            maxr = max(maxr, height[r])
            if height[l]<=height[r]:
                if height[l]<maxl:
                    total+=min(maxl,maxr)-height[l]
                l+=1
            else:
                if height[r]<maxr:
                    total+=min(maxl,maxr)-height[r]
                r-=1
            
        return total
                
                
    
            
            
        