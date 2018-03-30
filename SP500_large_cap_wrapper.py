"""
This wrapper file will create the __file_names.py that general_wrapper.py
imports and then import general_wrapper itself.

In the file are variables with the file names containing the data related to
the Standard and Poor 500 large capitalization stocks.

It also removes the SQLite file if it exists, so that a new file is created
rather than allow appending duplicate records to an existing file.

Key to naming conventions:
camelCase      global (and imported) variables and function parameters
CamelCase      class names
snake_case     variables not intended to be used globally and function names
"""


import os


fileNamesFile = '__file_names.py'

file_directory = 'SP500_large_cap'
bull_base_file = 'spy.us.txt'
bear_base_file = 'sh.us.txt'
bull_triple_file = 'upro.us.txt'
bear_triple_file = 'spxu.us.txt'
bullBaseFile = os.path.join(file_directory, bull_base_file)
bearBaseFile = os.path.join(file_directory, bear_base_file)
bullTripleFile = os.path.join(file_directory, bull_triple_file)
bearTripleFile = os.path.join(file_directory, bear_triple_file)
sqlFile = file_directory + '.sql'
plotFile = file_directory + '.html'

with open (fileNamesFile, mode='w') as file:
    file.write(  "bullBaseFile = r'" + bullBaseFile + "'\n" 
               + "bearBaseFile = r'" + bearBaseFile + "'\n"
               + "bullTripleFile = r'" + bullTripleFile + "'\n"
               + "bearTripleFile = r'" + bearTripleFile + "'\n"
               + "sqlFile = r'" + sqlFile + "'\n"
               + "plotFile = r'" + plotFile + "'\n")

if os.path.exists(sqlFile):
    os.remove(sqlFile)

from general_wrapper import *
