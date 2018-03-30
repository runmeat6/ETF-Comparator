"""
This file contains functions to help tidy the data.
The data is quite clean, so the only thing to do is normalize it.
By normalize, it is meant that the data points should match meaningfully.
The date field shall be used for that purpose.

Key to naming conventions:
camelCase      global (and imported) variables and function parameters
CamelCase      class names
snake_case     variables not intended to be used globally and function names
"""


def get_a_field_set_from_data(data, index=0):
    """
    Extract a unique (non-repeating) columnar set from supplied data

    It takes parameters:
    data (data in the form of a list of lists)
    and optionally:
    index (by default 0, it is the column field to extract)

    It returns a set of column field data scanned from all rows
    """
    return { row[index] for row in data }

def filter_rows_via_column_matching(data, column, index=0):
    """
    Filter data, by keeping rows whose particular field index matches the
    column criteria

    It takes parameters:
    data (data in the form of a list of lists)
    column (used as the match criteria for a particular field of the data)
    and optionally:
    index (by default 0, it is the data field used to match against column)

    Note that column can be many iterables, but probably ought to be a set

    It returns a filtered list of lists
    """
    return [ row for row in data if row[index] in column ]
