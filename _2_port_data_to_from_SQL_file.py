"""
This file has object models for saving exchange traded fund quote data;
a function for creating entries with just one transaction per call by using
the .atomic() decorator included with the Peewee ORM; additionally, there is
a function for retrieving the data from a given table.

Key to naming conventions:
camelCase      global (and imported) variables and function parameters
CamelCase      class names
snake_case     variables not intended to be used globally and function names
"""


from peewee import *
from __file_names import sqlFile


db = SqliteDatabase(sqlFile)

class Quote(Model):
    """
    The base model class used by Open, High, Low, and Close
    """
    date = DateField()
    bull_1x_price = FloatField()
    bear_1x_price = FloatField()
    bull_3x_price = FloatField()
    bear_3x_price = FloatField()

    class Meta:
        database = db

@db.atomic()
def add_quotes_to_table_from_data_sets(table, data1, data2, data3, data4, dateIndex=0):
    """
    Due to the .atomic() decorator, this function creates a table
    in the associated db file with just one bulk commit transaction

    It takes parameters:
    table (this is one of the Quote table models: Open, High, Low, or Close)
    data1 (the bull_1x data)
    data2 (the bear_1x data)
    data3 (the bull_3x data)
    data4 (the bear_3x data)
    and optionally:
    dateIndex (0 by default, it relates to the date field in the csv data)

    Note that the zip() function may not work if the data have not been date
    normalized, i.e. they must each have the same number of rows

    It has no return value
    """
    for data1row, data2row, data3row, data4row in zip(data1, data2, data3, data4):
        table.create(date = data1row[dateIndex],
                     bull_1x_price = data1row[table.index],
                     bear_1x_price = data2row[table.index],
                     bull_3x_price = data3row[table.index],
                     bear_3x_price = data4row[table.index])

def rationalize_quotes_from_table(table, rationalizeBase=10000):
    """
    Retrieve the data from the given table of the SQLite database

    It takes parameters:
    table (this is one of the Quote table models: Open, High, Low, or Close)

    It returns a tuple of lists
    """
    first_row = table.select().limit(1).get()
    rationalize_bull_1x_price = rationalizeBase / first_row.bull_1x_price
    rationalize_bear_1x_price = rationalizeBase / first_row.bear_1x_price
    rationalize_bull_3x_price = rationalizeBase / first_row.bull_3x_price
    rationalize_bear_3x_price = rationalizeBase / first_row.bear_3x_price
    indices = []
    dates = []
    bull_1x_prices = []
    bear_1x_prices = []
    bull_3x_prices = []
    bear_3x_prices = []
    for row in table.select():
        indices.append(row.id)
        dates.append(row.date)
        bull_1x_prices.append(row.bull_1x_price * rationalize_bull_1x_price)
        bear_1x_prices.append(row.bear_1x_price * rationalize_bear_1x_price)
        bull_3x_prices.append(row.bull_3x_price * rationalize_bull_3x_price)
        bear_3x_prices.append(row.bear_3x_price * rationalize_bear_3x_price)

    return indices, dates, bull_1x_prices, bear_1x_prices, bull_3x_prices, bear_3x_prices

class Open(Quote):
    """
    Class for the open table
    """
    index = 1 # Index associated with the csv open column data field

class High(Quote):
    """
    Class for the high table
    """
    index = 2 # Index associated with the csv high column data field

class Low(Quote):
    """
    Class for the low table
    """
    index = 3 # Index associated with the csv low column data field

class Close(Quote):
    """
    Class for the close table
    """
    index = 4 # Index associated with the csv close column data field

db.connect()
db.create_tables([Open, High, Low, Close], safe=True)
