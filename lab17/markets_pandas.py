import pandas as pd
import matplotlib.pyplot as plt

markets = pd.read_csv('farmers_markets.csv')
state_counts = markets['State'].value_counts()

state_counts.plot(kind='bar')
plt.xticks(rotation=90)
plt.xlabel('State')
plt.ylabel('Number of Farmers Markets')
plt.title('Farmers Markets by State')
plt.tight_layout()
plt.show()

# can we sort the farmers markets by alphabetcal order?
sorted_markets = markets.sort_values(by='MarketName')
print(sorted_markets['MarketName'].tolist())
# can we sort the list so its highest to lowest number of markets per state?
sorted_state_counts = state_counts.sort_values(ascending=False)
print(sorted_state_counts)

# can we print it in the order of the state with the highest percentage of markets accepting SNAP
markets_with_snap = markets[markets['SNAP'] == 'Y']
snap_state_counts = markets_with_snap['State'].value_counts()
snap_state_percentage = (
    snap_state_counts / state_counts * 100).sort_values(ascending=False)
print(snap_state_percentage)
