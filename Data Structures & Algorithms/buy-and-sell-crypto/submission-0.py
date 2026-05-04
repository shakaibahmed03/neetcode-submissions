class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price=float('inf')
        max_profit=0

        for right in range(len(prices)):
            min_price=min(min_price, prices[right])

            max_profit=max(max_profit, prices[right]-min_price)

        
        return max_profit

            





        
        