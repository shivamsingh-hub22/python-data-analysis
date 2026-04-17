import pandas as pd
df = pd.read_csv("C:\\Users\\HP\\Downloads\\archive (1)\\covid_india.csv")
print (df)

print (df.head())
print (df.tail())

import pandas as pd
df = pd.read_csv("C:\\Users\\HP\\Downloads\\archive (1)\\covid_india.csv")
import matplotlib.pyplot as plt
plt.plot(df['Name of State / UT'], df['Total Confirmed cases'])
plt.title('covid_india')
plt.xlabel('number of cases')
plt.ylabel('Death')
plt.show()