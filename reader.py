# importing pandas
import pandas as pd
  
# colspecs are a list of tuples that each specify the starting and end character indexes of each column value.
# ***REPLACE values in each tuple with the starting and end character values. 
colspecs = [(0, 13), (14, 29), (30, 40), (41, 52), (53, 59), (60, -1)]

# a list of the columns in the text 
# *** REPLACE with your own colummns
names=['gene_name', 'chromosomal_position', 'uniprot', 'entry_name', 'mtm_code', 'description']

# cleans a FWTF, takes a colspecs list, a list of column names, and reads into a DataFrame
# In this example, the first 36 and last 5 rows are ommitted in the file as they are not part of the data. These parameters
# will depend on your file. Full read_fwf documentation can be found here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_fwf.html 
df = pd.read_fwf('example_fwtf.txt', skiprows=36, skipfooter=5, colspecs=colspecs, names=names)

# display DataFrame with full rows/columns
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)

