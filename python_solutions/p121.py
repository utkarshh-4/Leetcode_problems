class Solution:
    def maxProfit(self, prices: list[int])->int:
        min_price=float('inf')
        profit=0

        for i in prices:
            min_price=min(min_price,i)
            profit=max(profit,i-min_price)
        return profit
