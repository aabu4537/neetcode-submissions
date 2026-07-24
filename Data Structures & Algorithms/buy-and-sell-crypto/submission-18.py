class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        best = 0
        l=0
        for r in range(1, len(prices)):
            print(r)
            if prices[r] < prices[l]:
                l = r
            best = max(best, prices[r]-prices[l])
        return best