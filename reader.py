# importing pandas
import pandas as pd
  
# read text file into pandas DataFrame, specifying delimeter as whitespace 
df = pd.read_csv("example_data.txt", delim_whitespace=True)
  
# display DataFrame
print(df)