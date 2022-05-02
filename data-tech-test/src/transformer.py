from typing import (
    List,
    Tuple,
)

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


class Transformer:

    def __init__(self):
        self

    def read_orders(self) -> pd.DataFrame:
        orders = pd.read_csv('../orders.csv', header=0)
        return orders

    def enrich_orders(self, orders: pd.DataFrame, col_name: str, value: List[str]) -> pd.DataFrame:
        """
        Adds a column to the data frame

        Args:
            orders (pd.Dataframe): The dataframe to be enriched
            col_name (str): Name of the new enriched column
            value (List[str]): Data to go into the new column

        Returns:
            The enriched dataframe
        """

        orders[col_name] = pd.Series(value)

        return orders

    def split_customers(self, orders: pd.DataFrame, threshold: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Splits customers into two groups based on a threshold

        Args:
            orders (pd.DataFrame): The dataframe to be split
            threshold (int): Value to split the customer base on

        Returns:
            Tuple containing the split dataframes
        """

        low_sc, high_sc = [amount for x, amount in orders.groupby(orders['amount'] >= threshold)]

        return low_sc, high_sc


if __name__ == '__main__':
    transformer = Transformer()
    data = transformer.read_orders()

    countries = ['GBR', 'AUS', 'USA', 'GBR', 'RUS', 'GBR', 'KOR', 'NZ']
    data = transformer.enrich_orders(data, 'Country', countries)

    data = transformer.enrich_orders(data, 'Country', countries)

    amount_list = data["amount"]
    threshold_list = [price for price in amount_list]
    threshold_split = int(input(f"Which amount would you like to split it {threshold_list} ? "))
    low_spending_customers, high_spending_customers = transformer.split_customers(data, threshold_split)

    # print(low_spending_customers)
    # print(high_spending_customers)


transformer = Transformer()
orders = transformer.read_orders()


# ----------- Bonus Task ------------

""" Extra bonus created for extra insights """
sns.relplot(data=orders,
            x="customer",
            y="amount",
            hue="date")
# plt.show()


# Question 1: Which customer placed the highest order amount ?
highest_order = orders["amount"].max()
customer_highest_order = orders[orders["amount"] == highest_order]["customer"]
# print(f"The customer with the highest orders is: {customer_highest_order}")


# Question 2: Which customer placed the lowest order amount ?
lowest_order = orders["amount"].min()
customer_lowest_orders = orders[orders["amount"] == lowest_order]["customer"]
# print(f"The customer with the lowest orders is: {customer_lowest_orders}")


# Question 3: What was the average order amount across all customers?
average_order = orders["amount"].mean()
# print(f"The average amount was: {average_order}")


# Question 4: Which customer placed the earliest order?
early_date = orders["date"].min()
customer_earliest_order = orders.loc[orders["date"] == early_date]["customer"]
# print(f"The customer who placed the earliest order was: {customer_earliest_order}")


# Question 5: In which month did most of the orders happen?
total_dates_list = [date for date in orders["date"]]
orders = pd.DataFrame({'StartDate': total_dates_list})
orders['StartDate'] = pd.to_datetime(orders['StartDate'])
orders['StartDate'].dt.to_period('M')
single_month = orders['StartDate'].dt.strftime('%m')
month = single_month.mode()
# print(f"The month with most orders is: {month}")
