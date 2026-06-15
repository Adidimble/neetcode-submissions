import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = sys.maxsize

        for i in prices:
            if mini>i:
                mini = i
            local_profit = i-mini
            if local_profit> profit:
                profit = local_profit
        
        return(profit)