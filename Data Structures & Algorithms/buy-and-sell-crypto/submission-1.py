class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp , rp = 0, 1 #lp is for buy and rp is for sell 
        # we need to buy the coin before we sell
        max_profit = 0

        #right pointer is incrementing till the end of the array
        while rp < len(prices):
            #for profit, we need to have selling prices
            if (prices[rp] > prices[lp]):
                profit = prices[rp] - prices[lp]
                max_profit = max(max_profit, profit)
            else:
                lp = rp
            rp +=1
        return max_profit
                 

        


