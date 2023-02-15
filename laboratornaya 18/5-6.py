#топ 10 хороших и топ 10 безответственных перевозчиков
import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

data = pd.read_csv('flight_delays.csv', sep=',')
data_1 = data[data['dep_delayed_15min'] == 'Y'].groupby('UniqueCarrier').dep_delayed_15min.count()
B = data_1.nlargest(10)
N = data_1.nsmallest(10)
print(B)
B.plot(x="UniqueCarrier", kind="bar", color = 'darkorange')
plt.show()
N.plot(x="UniqueCarrier", kind="bar", color = 'olive')
plt.show()
