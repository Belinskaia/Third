import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('flight_delays.csv', sep=',')
for i in range(1,13,1):
    data.loc[data["Month"] == 'c-'+str(i), "Month"] = i
data.sort_values(by='Month')
data_1 = data[data['dep_delayed_15min'] == 'Y'].groupby('Month').Origin.count()
data_2 = data.groupby('Month').Origin.count()
data_3 = data_1 / data_2
data_3.plot(kind='bar', x='Month', y='count')
plt.show()
