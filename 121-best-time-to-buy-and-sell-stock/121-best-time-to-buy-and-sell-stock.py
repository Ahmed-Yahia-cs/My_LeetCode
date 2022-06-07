class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, sell = 0, 1
        max_profit = 0
        
        while sell < len(prices):
            
            #calculate the profit
            profit = prices[sell] - prices[buy]
            
            #if the transaction is profitabel
            if profit > 0:
                max_profit = max(max_profit, profit)
                
            #if the transaction is not profitable
            elif profit < 0:
                buy = sell
            
            sell +=1
            
        return max_profit