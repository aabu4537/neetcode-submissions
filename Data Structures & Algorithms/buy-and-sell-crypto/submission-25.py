class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_p = float('inf')

        for p in prices:
            if p < min_p:
                min_p = p
            max_profit = max(max_profit, (p-min_p))


        return max_profit
        