import pandas as pd

# De esta forma leemos un archivo con pandas
data_frame = pd.read_csv('personas.csv')
data_frame2 = pd.read_csv('personas.csv')
print(data_frame)

# Data frame works with columns and rows, so if we want to access to a specific column values we do next
print('------------- single column ------------')
names_column = data_frame['Nombre']
print(names_column)

# Data frame from low to gith
print('------------ Desc order data frame (low to high) -----------')
order_data_frame = data_frame.sort_values('Edad')
print(order_data_frame)

# Data frame order from high to low
print('------------ Order data from high to low')
desc_order_data = data_frame.sort_values('Edad', ascending=False)
print(desc_order_data)

# To concat two data frames we can to next example
print('------ concat data frames -------')
df_concat = pd.concat([data_frame, data_frame2])
print(df_concat)

# Acces to rows and colums numbers
print('------ Number of rows and columns ---------')
rows_and_columns = data_frame.shape
print(rows_and_columns)