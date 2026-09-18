def maxProfit(prices):
    n = len(prices)
    res = 0

    for i in range(n-1):
        for j in range(i+1, n):
            res = max(res, prices[j] - prices[i])
    return res


def maxProfitOptimized(prices):
    minSoFar = prices[0]
    maxProfit = 0

    for i in range(1, len(prices)):
        #minimum price so far
        minSoFar = min(minSoFar, prices[i])

        #max profit so far
        maxProfit = max(maxProfit, prices[i] - minSoFar)
    return maxProfit




if __name__ == "__main__":
    #prices = [7, 10, 1, 3, 6, 9, 2]
    #prices = [1,2,3,4,5,6,7,8,9]
    prices = [9,8,7,6,5,4,3,2,1]
    #print(maxProfit(prices))  # Output: 8
    print(maxProfitOptimized(prices))  # Output: 8