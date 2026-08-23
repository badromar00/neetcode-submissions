class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        curr_buy = prices[0]
        maxProfit = 0
        for price in prices[1:]:
            maxProfit = max(maxProfit, price - curr_buy)
            if price < curr_buy:
                curr_buy = price
        return maxProfit


"""
if not prices: return 0

curr_buy = prices[0]
maxProfit = 0
for price in prices[1:]
    maxProfit = max(maxProfit, price - curr_buy)
    if price < curr_buy:
        curr_buy = price

return maxProfit




curr_buy = 1
maxProfit = 4

        p
[10,1,5,6,7,1]

"""