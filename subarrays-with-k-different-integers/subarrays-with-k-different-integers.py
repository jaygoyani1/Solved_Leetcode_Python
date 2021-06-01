class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def helper(arr,k):
            count = collections.Counter()
            start = 0
            total = 0
            for ind,val in enumerate(arr):
                if count[val] == 0:
                    k-=1
                count[val] += 1
                while k <0:
                    count[arr[start]] -=1
                    if count[arr[start]] == 0:
                        k+=1
                    start += 1
                total += ind-start+1
            return total
        return helper(nums,k) - helper(nums,k-1)
                    
        