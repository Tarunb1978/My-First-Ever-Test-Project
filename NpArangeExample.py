import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''matrix_data = np.arange(0, 30 * 3, 3)
matrix = matrix_data.reshape(10, 3)
print(matrix)
print(matrix.shape)
my_series = pd.Series(matrix_data)
print(my_series.shape)
print(my_series.iloc[0:10])
print(my_series.iloc[1])
my_df = pd.DataFrame(matrix)
print(my_series)
print(my_df)
'''

uber_df = pd.read_csv(r"C:\Users\tarun\OneDrive\Learning\Data\UberDrives2016.csv")
#uber_df["PURPOSE*"].value_counts().plot.bar()
#plt.show()
print(uber_df["CATEGORY*"].unique())
select_condition = (uber_df['CATEGORY*'] == 'Personal' ) 
#print("The SELECT Condition is = \n",    select_condition)
print("Number of True values:\n", select_condition.sum())
'''print("DataFrame shape before filter:", uber_df.shape)
print("DataFrame head before filter:")
print(uber_df.head())
print("Rows that meet the condition:")
print(uber_df[select_condition])
print("uber_df index:", uber_df.index)
print("select_condition index:", select_condition.index)
print("Do indexes match?", uber_df.index.equals(select_condition.index))
'''
#print((uber_df['CATEGORY*'] == 'Personal').sum())
uber_df = uber_df[select_condition] 
print(uber_df)
#uber_df = uber_df.dropna()
#print(uber_df)

#print(uber_df.shape)
#print(uber_df.head())
      
#uber_df.sort_values(by = 'START*', 'MILES*' ] , ascending== [True , False] inplace=True)

'''
#print(uber_df)
#
#uber_df = uber_df[uber_df['Base'] == 'B02512']
#print(uber_df.shape)
#print(uber_df.iloc[1:10, [0, 1, 2, 3, 4, 5]])
# uber_df = uber_df[uber_df['Date/Time'].str.contains('2016-01-01')]
uber_df['Date/Time'] = pd.to_datetime(uber_df['Date/Time']) 
uber_df = uber_df.set_index('Date/Time')
uber_df = uber_df.sort_index()
uber_df = uber_df[['Lat', 'Lon']]


uber_df = uber_df.resample('H').mean()
uber_df = uber_df.dropna()
uber_df = uber_df.reset_index()
uber_df['Date/Time'] = uber_df['Date/Time'].dt.strftime('%Y-%m-%d %H:%M:%S')
uber_df = uber_df.set_index('Date/Time')        
uber_df = uber_df.sort_index()
uber_df = uber_df.reset_index() 
uber_df['Date/Time'] = pd.to_datetime(uber_df['Date/Time']) 
uber_df = uber_df.set_index('Date/Time')    
uber_df = uber_df.sort_index()
'''