class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            a= max(nums[0],nums[1])
            return a
        t=[0]*n
        t[0]=nums[0]
        t[1]= max(nums[0], nums[1])
        
        for i in range(2,n):
            t[i]= max(nums[i]+t[i-2], t[i-1])
            
        return t[-1]