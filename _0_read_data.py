"""
This file has the function to read in the data

Key to naming conventions:
camelCase      global (and imported) variables and function parameters
CamelCase      class names
snake_case     variables not intended to be used globally and function names
"""


import csv


def load_data_with_csv(fileName, delimiterCharacter=',', headerRowsToSkip=1):
    """
    By default, this function reads comma separated value data
    and skips one header row

    It takes parameters:
    fileName (path included as part of it)
    and optionally:
    delimiterCharacter (data separation character)
    headerRowsToSkip (number of rows at the head that are not part of the data)
 
    It returns a list slice starting after the headerRowsToSkip through the end
    """
    csv_list = None # establish the csv_list variable outside of the with scope
    with open(fileName, encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=delimiterCharacter)
        csv_list = [ row for row in csv_data ]
    return csv_list[headerRowsToSkip:]
