# FW-Text-File-into-Dataframe-Reader

Python code to convert a fixed-width text file (FWTF) of data columns into a dataframe. A definition of a FWTF can be found here: https://www.softinterface.com/Convert-XLS/Features/Fixed-Width-Text-File-Definition.htm 

FWTFs cannot be read as a delimited file (comma, tab, etc) because each column is padded by a specified number of characters. In the example text file used, each padded character is a whitespace character. 

This is an example program. Parameters/values in reader.py can be changed to match another file used. In the colspecs list, you will need to know the starting and end character indexes of your own file and replace the values accordingly. 

Reference links for the code:
https://towardsdatascience.com/parsing-fixed-width-text-files-with-pandas-f1db8f737276 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_fwf.html
