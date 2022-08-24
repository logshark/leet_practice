#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

#        max_profit = 0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 profit = prices[j] - prices[i]
#                 if profit > max_profit:
#                     max_profit = profit

        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if min_price > price:
                min_price = price

            profit = price - min_price
            print(profit)
            if profit > max_profit:
                max_profit = profit

        # print(max_prifit)

        return max_profit

# @lc code=end

