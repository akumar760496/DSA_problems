def maxProfit(stock_prices):
    max_profit = 0
    best_buy = stock_prices[0]

    for i in range(len(stock_prices)):
        if stock_prices[i] > best_buy:
            max_profit = max(max_profit, stock_prices[i]-best_buy)

        best_buy = min(best_buy, stock_prices[i])
    return max_profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(stock_prices= prices))