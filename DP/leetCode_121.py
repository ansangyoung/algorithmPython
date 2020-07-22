#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#problem 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(prices):
        res = 0
        pricesLen = len(prices)
        if pricesLen > 0:
            min = prices[0]
            for i in range(1, pricesLen):
                if min > prices[i]:
                    min = prices[i]
                if min < prices[i]:
                    if prices[i] - min > res:
                        res = prices[i] - min
        return res
    #print(maxProfit([7,1,5,3,6,4]))
    #print(maxProfit([7,6,4,3,1]))
    #print(maxProfit([1,2]))