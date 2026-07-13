# ------------------------------------------------------------
# Problem: Best Time to Buy and Sell Stock
# ------------------------------------------------------------
# Problem Statement:
# You are given an array 'prices' where prices[i] represents the
# price of a stock on the i-th day.
#
# You are allowed to:
#   1. Buy the stock only once.
#   2. Sell the stock only once.
#   3. You must buy before you sell.
#
# Return the maximum profit that can be achieved.
# If no profit is possible, return 0.
#
# Example:
# Input : [7, 1, 5, 3, 6, 4]
# Output: 5
#
# Explanation:
# Buy at price = 1
# Sell at price = 6
# Profit = 6 - 1 = 5
#
# Approach:
# - Keep track of the minimum stock price seen so far.
# - For every day's price, calculate the profit if we sell today.
# - Update the maximum profit whenever a better profit is found.
# - Update the minimum price whenever a smaller price is found.
#
# Time Complexity : O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

def maximum_profit(prices):

    # Assume the first day's price is the minimum buying price
    mini = prices[0]

    # Initially, no profit has been made
    max_profit = 0

    # Traverse the array from the second day
    for i in range(1, len(prices)):

        # Calculate profit if we sell the stock today
        profit = prices[i] - mini

        # Update the maximum profit
        max_profit = max(max_profit, profit)

        # Update the minimum buying price
        mini = min(mini, prices[i])

    return max_profit


# ---------------- Driver Code ----------------

prices = [7, 1, 5, 3, 6, 4]

print("Maximum Profit:", maximum_profit(prices))