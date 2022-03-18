def price(share):
    return share[1]


def percent(share):
    return share[2]


def profit(share):
    gain = (float(share[1]) * float(share[2])) / 100
    return gain


def greedy(available_shares, total_assets_available, key_func=profit):
    share_package = []
    share_package_price = 0
    share_package_profit = 0
    shares_sorted = sorted(available_shares, key=key_func)
    while len(shares_sorted) > 0:
        share = shares_sorted.pop()
        if price(share) + share_package_price <= total_assets_available:
            share_package.append(share)
            share_package_price += price(share)
            share_package_profit += profit(share)
    return share_package, share_package_price, share_package_profit
