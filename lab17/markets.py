import csv
from collections import Counter
import matplotlib.pyplot as plt

with open('farmers_markets.csv', 'r', encoding='utf-8') as file:
    markets = list(csv.DictReader(file))


'''def california_market_names():
    return [m['MarketName'] for m in markets if m['State'] == 'California']
print("California Markets:", california_market_names())


def alaska_market_names():
    return [m['MarketName'] for m in markets if m['State'] == 'Alaska']
print("Alaska Markets:", alaska_market_names())'''


def market_names_in_state(state):
    return [m['MarketName'] for m in markets if m['State'] == state]

# markets that sell nuts


def markets_selling_nuts():
    return [m for m in markets if m['Nuts'] == 'Y']

# markets in Maine that sell nuts but not seafood


def markets_in_maine_selling_nuts_but_not_seafood():
    return [
        m
        for m in markets
        if m['State'] == 'Maine' and m['Nuts'] == 'Y' and m['Seafood'] == 'N'
    ]

# west of 100 that also have youtube channels


def markets_with_you_tube_west_of_100():
    return [
        (m['MarketName'], m['street'], m['city'], m['zip'])
        for m in markets
        if float(m['x']) < -100 and m['Youtube'] != ''
    ]

# not a dictionary, a counter - but there is a way we can turn it into a dictionary (shown below in the return statement)


def market_counts_by_state():
    return dict(Counter(m['State'] for m in markets))


def plot_market_histogram():
    state_counts = market_counts_by_state()
    plt.bar(state_counts.keys(), state_counts.values())
    plt.xticks(rotation=90)
    plt.xlabel('State')
    plt.ylabel('Number of Farmers Markets')
    plt.title('Farmers Markets by State')
    plt.tight_layout()
    plt.show()


# when computer scientists work with data, there are so many patterns that they have created libraries to help make these tasks simpler
plot_market_histogram()
# print(market_counts_by_state())

# print("California Markets:", market_names_in_state('California'))
# print("Alaska Markets:", market_names_in_state('Alaska'))
# print("New York Markets:", market_names_in_state('New York'))
# print("Texas Markets:", market_names_in_state('Texas'))
