class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        def rob1(nums):
            print(nums)
            if not nums:
                return 0
            if len(nums) <= 2:
                return max(nums)
            dp = [0]* len(nums)
            
            dp[0] = nums[0]
            dp[1] = max(nums[1],nums[0])

            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])

            return dp[-1]
    
        return max(rob1(nums[:-1]), rob1(nums[1:]))
        