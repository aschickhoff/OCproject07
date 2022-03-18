def get_all_combinations(available_shares):
    package_combinations = [[]]
    for share in available_shares:
        new_package = [s + [share] for s in package_combinations]
        package_combinations.extend(new_package)
    return package_combinations


def brute_force(available_shares, total_assets_available):
    share_package = []
    best_price = 0
    best_profit = 0
    for share_combination in get_all_combinations(available_shares):
        set_price = sum([share[1] for share in share_combination])
        set_profit = sum([(share[1] * share[2]) / 100 for share in share_combination])
        if set_profit > best_profit and set_price <= total_assets_available:
            best_profit = set_profit
            best_price = set_price
            share_package = share_combination
    return share_package, best_price, best_profit
