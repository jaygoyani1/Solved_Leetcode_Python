class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) -1 
        maxl = height[left]
        maxr = height[right]
        
        ans = 0
        
        while left<right:
            
            maxl = max(height[left],maxl)
            maxr = max(height[right],maxr)
            common = min(maxl,maxr)
            
            if height[left]< height[right]:
                if height[left]<common:
                    ans += common-height[left]
                left+=1
            else:
                if height[right]<common:
                    ans += common-height[right]
                right-=1
        return ans
                
            
        