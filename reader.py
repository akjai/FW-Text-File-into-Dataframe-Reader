# importing pandas
import pandas as pd
  
# read text file into pandas DataFrame and create 
# header with names
df = pd.read_csv("example_data.txt", delim_whitespace=True)
  
# display DataFrame
print(df)