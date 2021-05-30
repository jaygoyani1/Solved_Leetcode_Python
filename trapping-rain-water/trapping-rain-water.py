class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left_max = height[0]
        right_max = height[-1]
        left = 1
        right = len(height)-2
        
        maximum = 0
        while left<=right:
            left_max = max(left_max,height[left])
            right_max = max(right_max,height[right])
            
            if left_max <= right_max:
                maximum += (left_max - height[left])
                left+=1
            else:
                maximum += (right_max - height[right])
                right-=1
        
        return maximum
        