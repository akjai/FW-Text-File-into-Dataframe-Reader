# FW-Text-File-into-Dataframe-Reader

Python code to convert a fixed-width text file (FWTF) of data columns into a dataframe. A definition of a FWTF can be found here: https://www.softinterface.com/Convert-XLS/Features/Fixed-Width-Text-File-Definition.htm 

FWTFs cannot be read as a delimited file (comma, tab, etc) because each column is padded by a specified number of characters. In the example text file used, each padded character is a whitespace character. 

The highlighted blue characters in the example file indicate the range of characters of the first columns being 0-13. This will be our first tuple in our colspecs list in reader.py. 

<img width="890" alt="image" src="https://user-images.githubusercontent.com/55563026/177579250-c107cd7f-71bd-4da2-9c85-cfab8be42d09.png">


This is an example program. Parameters/values in reader.py can be changed to match another file used. In the colspecs list, you will need to know the starting and end character indexes of your own file and replace the values accordingly. 

To run the program, the text file must be in the same directory as reader.py. 

Reference links for the code:
https://towardsdatascience.com/parsing-fixed-width-text-files-with-pandas-f1db8f737276 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_fwf.html
