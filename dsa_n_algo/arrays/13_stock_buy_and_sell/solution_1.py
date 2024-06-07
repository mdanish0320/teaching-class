"""
Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. 
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input:
 prices = [7,1,5,3,6,4]
Output:
 5
Explanation:
 Buy on day 2 (price = 1) and 
sell on day 5 (price = 6), profit = 6-1 = 5.

Note
: That buying on day 2 and selling on day 1 
is not allowed because you must buy before 
you sell.
"""

arr = [7,1,5,3,6,4]
lowest_stock = 10000000
lday = 0
highest_stock = 0

# find lowest number and the index
for i in range(len(arr)):
    if arr[i] < lowest_stock:
        lowest_stock = arr[i]
        lday = i

# find highest number that also greater than the buying day
for i in range(len(arr)):
    if arr[i] > highest_stock and i > lday:
        highest_stock = arr[i]

print(lowest_stock, highest_stock, highest_stock - lowest_stock)
