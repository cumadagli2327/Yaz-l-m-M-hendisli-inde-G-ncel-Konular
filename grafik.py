import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('veri.csv',parse_dates=['Tarih'],index_col=['Tarih'])
df=pd.DataFrame(data)
df=(df-df.min())/(df.max()-df.min())
df=df.fillna(df.mean())
df.info()
df = df.drop(['O3'],axis=1)
df.info()
pm10= df.PM10.resample('M').mean().plot()
no= df.NO.resample('M').mean().plot()
nox= df.NOX.resample('M').mean().plot()
no2= df.NO2.resample('M').mean().plot()
so2= df.SO2.resample('M').mean().plot()
co= df.CO.resample('M').mean().plot()
plt.show()
