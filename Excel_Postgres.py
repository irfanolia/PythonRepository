import pandas as pd
from sqlalchemy import create_engine

# Load the Excel file
#df = pd.read_excel('/Users/irfanolia/OneDrive/Documents/Book1.xlsx',sheet_name='Sheet1')
df = pd.read_excel('/Users/irfanolia/OneDrive/Documents/ExcelSheets/Excel102Exercises.xlsx',sheet_name='Order Info')

# Create a connection to the PostgreSQL database
engine = create_engine('postgresql://postgres:KarachI01!@localhost:3010/postgres')


# Insert data into PostgreSQL table
#df.to_sql('heatmap', con=engine, if_exists='replace', index=False)
df.to_sql('order_info', con=engine, if_exists='replace', index=False)


print("Data inserted successfully!")

#conn = psycopg2.connect(
    # dbname="irfanolia",
 #   dbname="postgres",
  #  user="postgres",
   # password="KarachI01!",
    #host="localhost",
    #port="3010"
#)

# Create a cursor object
#cursor = conn.cursor()
# Display the first few rows of the dataframe
print(df.head())




