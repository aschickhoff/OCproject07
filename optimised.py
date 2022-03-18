def price(share):
    return share[1]


def percent(share):
    return share[2]


def profit(share):
    gain = (float(share[1]) * float(share[2])) / 100
    return gain


def dynamic(available_shares, total_assets_available):
    # conversion to "cent" to match with price and profit
    total_assets_available_cent = total_assets_available * 100
    total_shares = len(available_shares)
    total_shares_price = []
    total_profit = []
    best_shares_package = []
    share_package_price = 0
    share_package_profit = 0

    # conversion to "cent" to avoid floats in table/matrix
    for share in available_shares:
        total_shares_price.append(int(share[1]*100))
        total_profit.append(((share[1] * 100) * share[2]) / 100)

    # building the table / matrix with all solutions of the sub-problems
    dp = [[0 for x in range(total_assets_available_cent + 1)] for y in range(total_shares + 1)]

    # first row/column is 0, starting therefore with 1
    for row in range(1, total_shares + 1):
        for column in range(1, total_assets_available_cent + 1):
            if total_shares_price[row-1] <= column:
                dp[row][column] = max(total_profit[row-1] + dp[row-1][column-total_shares_price[row-1]], dp[row-1][column])
            else:
                dp[row][column] = dp[row-1][column]

    # get information from picked shares until they are all processed
    while total_assets_available_cent >= 0 and total_shares >= 0:
        if dp[total_shares][total_assets_available_cent] == dp[total_shares-1][total_assets_available_cent - total_shares_price[total_shares-1]] + total_profit[total_shares-1]:
            best_shares_package.append(available_shares[total_shares-1])
            total_assets_available_cent -= total_shares_price[total_shares-1]
            share_package_price += price(available_shares[total_shares-1])
            share_package_profit += profit(available_shares[total_shares-1])
        total_shares -= 1
    return best_shares_package, share_package_price, share_package_profit
