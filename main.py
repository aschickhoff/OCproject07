import csv
import time
import bruteforce
import optimised
import greedy

AMOUNT_TO_INVEST = 500
# FILE_TO_USE = "data/dataset20.csv"
# FILE_TO_USE = "data/dataset1_Python+P7.csv"
FILE_TO_USE = "data/dataset2_Python+P7.csv"


# data_shares = [(name, price, profit)]
def get_shares_data():
    with open(FILE_TO_USE, "r") as data:
        csv_reader = csv.reader(data)
        next(csv_reader)
        data_shares = []
        for row in csv_reader:
            if float(row[1]) <= 0 or float(row[2]) <= 0:
                pass
            else:
                shares = (row[0], float(row[1]), float(row[2]))
                data_shares.append(shares)
        return data_shares


def main():
    shares = get_shares_data()

    if FILE_TO_USE == "data/dataset20.csv":
        start_time = time.time()
        shares_packet, opt_price, opt_profit = bruteforce.brute_force(shares, AMOUNT_TO_INVEST)
        print(f"\nBrute force method took: {(time.time() - start_time)} sec\n")
        for item in shares_packet:
            print(f"{item[0]}: Price: {item[1]}€ - Profit: {round((item[1] * item[2]) / 100, 2)}€")
        print(f"We invest: {round(opt_price, 2)}€\nProfit: {round(opt_profit, 2)}€ after 2 years.\n")

    start_time = time.time()
    shares_packet, opt_price, opt_profit = greedy.greedy(shares, AMOUNT_TO_INVEST, greedy.price)
    print(f"\nGreedy method (sorted by price) took: {(time.time() - start_time)} sec\n")
    for item in shares_packet:
        print(f"{item[0]}: Price: {item[1]}€ - Profit: {round((item[1] * item[2]) / 100, 2)}€")
    print(f"\nWe invest: {round(opt_price, 2)}€\nProfit: {round(opt_profit, 2)}€ after 2 years.\n")

    start_time = time.time()
    shares_packet, opt_price, opt_profit = greedy.greedy(shares, AMOUNT_TO_INVEST, greedy.percent)
    print(f"\nGreedy method (sorted by percent) took: {(time.time() - start_time)} sec\n")
    for item in shares_packet:
        print(f"{item[0]}: Price: {item[1]}€ - Profit: {round((item[1] * item[2]) / 100, 2)}€")
    print(f"\nWe invest: {round(opt_price, 2)}€\nProfit: {round(opt_profit, 2)}€ after 2 years.\n")

    start_time = time.time()
    shares_packet, opt_price, opt_profit = greedy.greedy(shares, AMOUNT_TO_INVEST, greedy.profit)
    print(f"\nGreedy method (sorted by profit) took: {(time.time() - start_time)} sec\n")
    for item in shares_packet:
        print(f"{item[0]}: Price: {item[1]}€ - Profit: {round((item[1] * item[2]) / 100, 2)}€")
    print(f"\nWe invest: {round(opt_price, 2)}€\nProfit: {round(opt_profit, 2)}€ after 2 years.\n")

    start_time = time.time()
    shares_packet, opt_price, opt_profit = optimised.dynamic(shares, AMOUNT_TO_INVEST)
    print(f"\nDynamic method took: {(time.time() - start_time)} sec\n")
    for item in shares_packet:
        print(f"{item[0]}: Price: {item[1]}€ - Profit: {round((item[1] * item[2]) / 100, 2)}€")
    print(f"\nWe invest: {round(opt_price, 2)}€\nProfit: {round(opt_profit, 2)}€ after 2 years.\n")


if __name__ == "__main__":
    main()
