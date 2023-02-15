#топ 5 направлений, для которых чаще всего происходят задержки
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('flight_delays.csv', sep=',')
data_1 = data[data['dep_delayed_15min'] == 'Y'].groupby('Dest').dep_delayed_15min.count()
D = data_1.nlargest(5)
print(D)
