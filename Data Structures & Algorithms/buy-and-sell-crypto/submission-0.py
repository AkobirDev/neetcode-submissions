class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for price in prices:
            if price > buy:
                max_profit = max(max_profit, price - buy)
            
            else:
                buy = price
        
        return max_profit