def maxProfit(arr):
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        maxPro = max(maxPro, arr[i] - minPrice)
    return maxPro

arr = [7, 2, 5, 3, 6, 1, 8]
maxPro = maxProfit(arr)
print("Max profit is:", maxPro)