#задержки рейсов по временам года
import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

data = pd.read_csv('flight_delays.csv', sep=',')
for i in range(1, 13, 1):
    if i in [1, 2, 12]:
        data.loc[data["Month"] == 'c-'+str(i), "Month"] = 'Winter'
    elif i in [3, 4, 5]:
        data.loc[data["Month"] == 'c-' + str(i), "Month"] = 'Spring'
    elif i in [6, 7, 8]:
        data.loc[data["Month"] == 'c-'+str(i), "Month"] = 'Summer'
    else:
        data.loc[data["Month"] == 'c-'+str(i), "Month"] = 'Autumn'
data = data.rename(columns={"Month": "Seasons"})
data_1 = data[data['dep_delayed_15min'] == 'Y'].groupby('Seasons').dep_delayed_15min.count()
print(data_1)
data_1.plot(kind='pie', colors = ("orangered", "limegreen", "magenta", "royalblue"))
plt.show()
