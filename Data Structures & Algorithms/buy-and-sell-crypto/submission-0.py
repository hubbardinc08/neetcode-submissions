class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_lst = []
        min_val = -1
        profit = 0

        for i in range(len(prices)):
            curr_lst.append(prices[i])
            if (len(curr_lst) == 1):
                min_val = prices[i]
                continue
            
            if (prices[i] < min_val):
                min_val = prices[i]
            
            if (prices[i] - min_val > profit):
                profit = prices[i] - min_val
        
        return profit

            