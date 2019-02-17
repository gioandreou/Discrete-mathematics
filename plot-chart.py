import xlsxwriter
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("xlsx-descrete-step5.xlsx")
labels=list(df.columns.values)
ax = plt.gca()
df.plot(kind='line',x=labels[0],y=labels[1],ax=ax)

plt.savefig("N-time_chart.png")
#commnetß