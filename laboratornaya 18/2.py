import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('flight_delays.csv', sep=',')
data_1 = data[data['dep_delayed_15min'] == 'Y'].groupby('Distance').Origin.count()
data_1.plot(kind='line', x='Distance', y='count')
plt.show()
