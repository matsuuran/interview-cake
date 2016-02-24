def get_max_profit(stock_prices_yesterday):
	if len(stock_prices_yesterday) < 2:
		return

	min_price = stock_prices_yesterday[0]
	max_profit = stock_prices_yesterday[1]-stock_prices_yesterday[0]

	for index, current_price in enumerate(stock_prices_yesterday):
		if index == 0:
			continue

		min_price = min(min_price, current_price)
		potential_profit = current_price-min_price
		max_profit = max(max_profit, potential_profit)

	return max_profit

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)