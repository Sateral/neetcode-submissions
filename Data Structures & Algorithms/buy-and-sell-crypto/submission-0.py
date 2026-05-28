class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        r = 0
        buy = prices[0]
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            
            print(buy, prices[i])
            r = max(r, prices[i] - buy)

        return r