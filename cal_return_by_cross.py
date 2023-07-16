import pandas as pd
import matplotlib.pyplot as plt

import utility


def cal_return_by_cross(data, fast_ma, slow_ma, commission_fee):
    golden_cross = utility.get_golden_cross(data, fast_ma, slow_ma)
    death_cross = utility.get_death_cross(data, fast_ma, slow_ma)

    money_invest = 1000000000
    money_hold = money_invest
    hold = 0
    trade_times = 0

    sr1 = pd.Series(1, index=golden_cross)
    sr2 = pd.Series(0, index=death_cross)

    sr = sr1._append(sr2).sort_index()

    for i in range(0, len(sr)):
        price = data[sr.index[i]]
        if sr.iloc[i] == 1:
            # golden cross
            hold = money_hold // price
            money_hold -= hold*price
            trade_times += 1
        else:
            # death cross
            money_hold += hold*price
            hold = 0
            trade_times += 1

    price = data[-1]
    total_money = hold * price + money_hold - commission_fee*trade_times

    return (total_money / money_invest), trade_times


if __name__ == "__main__":
    data = pd.read_csv('data/MSFT.csv', index_col='Date')

    return_rate, trade_times = cal_return_by_cross(data['Open'], 5, 20, 10)
    print("Trade times: " + str(trade_times))
    print("Total return rate: " + str(return_rate))
    print("Total return (10000): " + str(return_rate * 10000))

    print(data.index[0])
    print(data.index[-1])
