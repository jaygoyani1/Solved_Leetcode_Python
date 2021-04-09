class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        prev = curr = 0
        last = None
        for i in sorted(count):
            if i-1 != last:
                curr,prev = curr+ i*count[i], curr
            else:
                curr,prev = max(prev + i*count[i],curr), curr
            last = i
        return curr
        
        