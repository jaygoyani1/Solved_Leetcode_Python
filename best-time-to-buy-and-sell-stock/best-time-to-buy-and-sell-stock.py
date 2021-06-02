class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float("inf")
        profit = 0
        for i in prices:
            if i < minimum:
                minimum = i
            elif i-minimum > profit:
                profit = i-minimum
        return profit