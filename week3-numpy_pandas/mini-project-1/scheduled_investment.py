# 注意 - Copy this file and rename as scheduled_investment_{first_name}.py then complete code with a PR.
# 注意 - Copy this file and rename as scheduled_investment_{first_name}.py then complete code with a PR.
# 注意 - Copy this file and rename as scheduled_investment_{first_name}.py then complete code with a PR.

""" DO NOT EDIT (BEGIN) """
import pandas as pd
import datetime as dt

RAW_DATA_NAME = "data/QQQ.csv"
ANALYSIS_RESULT_DATA_NAME = "data/QQQ-result.csv"


def read_data() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_NAME)


def write_data(data: pd.DataFrame, file_name: str = ANALYSIS_RESULT_DATA_NAME) -> None:
    return data.to_csv(file_name, index=False)


def is_monday(day: str) -> bool:
    return dt.datetime.strptime(day, '%Y-%m-%d').strftime('%A') == 'Monday'


# 从年数，回报倍数得到年化收益. e.g. 0.1 -> 10% 年化收益
def annual_return(num_of_year: int, times: float) -> float:
    return pow(times, 1 / num_of_year) - 1.0


""" DO NOT EDIT (END) """


# -- TODO: Part 1 (START)
def calculate_scheduled_investment(data: pd.DataFrame) -> ():
    shares = 10  # 每次购买 10 share QQQ
    positions = [0.0]
    cost = [0.0]
    assets = [0.0]
    for i in range(1, len(data)):
        open_price = data.iloc[i]['OPEN']
        date = data.iloc[i]['DATES']
        # 实现计算方程，每个周一购买shares，其他日期不购买
        #   如果购买，需要增加position仓位，增加cost花费
        #   如果不购买，append前日仓位和花费
        #   然后总需要根据open_price计算asset, 并且加入assets
        if is_monday(date):
            positions.append(positions[-1] + 10)
        else:
            positions.append(positions[-1])
        assets.append(open_price * positions[-1])
    print(len(positions))
    return positions, cost, assets


# -- TODO: Part 1 (END)


# -- TODO: Part 2 (START)
def export_result() -> float:
    # 生成 {first_name}_QQQ-result.csv, 目标是跟QQQ-result-expected.csv 一致
    # 在这里调用 calculate_scheduled_investment, 并且赋值
    # 到asset 和cost.
    # 最后返回十年的年化率
    asset = [1]  # replace
    cost = [1]  # replace
    return annual_return(10, asset[-1] / cost[-1])  # 10 years


# -- TODO: Part 2 (END)


if __name__ == '__main__':
    print(calculate_scheduled_investment(read_data()))
    # print("Investment Return: ", export_result())
