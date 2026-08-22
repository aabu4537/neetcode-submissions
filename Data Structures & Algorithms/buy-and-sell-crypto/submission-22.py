class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_price = 0
        min_price = float('inf')

        for p in prices:
            if min_price > p:
                min_price = p
            max_price = max(max_price, p-min_price)

        return max_price
        