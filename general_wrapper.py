"""
This wrapper file will import and call all the necessary functions
to read, normalize, and create a SQL DB and visualization of data
related to the a set of given stock quote data.

The graph will include plots related to various index exchange traded funds:
long stock (bull) non-leveraged (base),
short stock (bear) non-leveraged (base),
long stock (bull) 3x margin leveraged (triple),
and short stock (bear) 3x margin leveraged (triple).

Key to naming conventions:
camelCase      global (and imported) variables and function parameters
CamelCase      class names
snake_case     variables not intended to be used globally and function names
"""


"""
Read data
"""

from _0_read_data import load_data_with_csv as load_data
from __file_names import (bullBaseFile, bearBaseFile,
                          bullTripleFile, bearTripleFile)

bull_base_raw_data = load_data(bullBaseFile)
bear_base_raw_data = load_data(bearBaseFile)
bull_triple_raw_data = load_data(bullTripleFile)
bear_triple_raw_data = load_data(bearTripleFile)

"""
Filter data
"""

from _1_filter_data import (get_a_field_set_from_data as get_dates_from,
                            filter_rows_via_column_matching as filter_by_date)

bull_base_dates = get_dates_from(bull_base_raw_data)
bear_base_dates = get_dates_from(bear_base_raw_data)
bull_triple_dates = get_dates_from(bull_triple_raw_data)
bear_triple_dates = get_dates_from(bear_triple_raw_data)

dates = bull_base_dates & bear_base_dates & bull_triple_dates & bear_triple_dates

bull_base_data = filter_by_date(bull_base_raw_data, dates)
bear_base_data = filter_by_date(bear_base_raw_data, dates)
bull_triple_data = filter_by_date(bull_triple_raw_data, dates)
bear_triple_data = filter_by_date(bear_triple_raw_data, dates)

del bull_base_dates
del bear_base_dates
del bull_triple_dates
del bear_triple_dates
del dates
del bull_base_raw_data
del bear_base_raw_data
del bull_triple_raw_data
del bear_triple_raw_data

"""
Export data to SQL file
"""

from _2_port_data_to_from_SQL_file import *

add_quotes_to_table_from_data_sets(Open, bull_base_data, bear_base_data,
                                   bull_triple_data, bear_triple_data)
add_quotes_to_table_from_data_sets(High, bull_base_data, bear_base_data,
                                   bull_triple_data, bear_triple_data)
add_quotes_to_table_from_data_sets(Low, bull_base_data, bear_base_data,
                                   bull_triple_data, bear_triple_data)
add_quotes_to_table_from_data_sets(Close, bull_base_data, bear_base_data,
                                   bull_triple_data, bear_triple_data)

db.close()
del bull_base_data
del bear_base_data
del bull_triple_data
del bear_triple_data

"""
Import data from SQL file and visualize data
"""

from _3_visualize_data import *

