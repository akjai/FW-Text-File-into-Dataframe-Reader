# importing pandas
import pandas as pd
  
# colspecs are a list of tuples that each specify the starting and end character indexes of each column value 
colspecs = [(0, 14), (14, 30), (30, 41), (41, 53), (53, 60), (60, -1)]

# a list of the columns in the text 
names=['gene_name', 'chromosomal_position', 'uniprot', 'entry_name', 'mtm_code', 'description']

# cleans a FWTF, takes a colspecs list, a list of column names, and reads into a DataFrame
# read_fwf documentation can be found here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_fwf.html 
df = pd.read_fwf('example_fwtf.txt', skiprows=36, skipfooter=5, colspecs=colspecs, names=names)

# display DataFrame
print(df)

