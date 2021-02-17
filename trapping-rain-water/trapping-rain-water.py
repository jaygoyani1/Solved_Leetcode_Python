class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        leftmax = 0
        rightmax = 0
        ans = 0
        while left <= right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            
            if height[left] <= height[right]:
                ans += min(leftmax,rightmax) - height[left]
                left += 1
            
            else:
                ans += min(leftmax,rightmax) - height[right]
                right -= 1
        return ans
            
            
        