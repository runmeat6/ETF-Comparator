"""
This file has imports and uses functions for retrieving data from the SQLite
file and then visualizing that data

Key to naming conventions:
camelCase      global (and imported) variables and function parameters
CamelCase      class names
snake_case     variables not intended to be used globally and function names
"""


from bokeh.plotting import figure, output_file, show
from _2_port_data_to_from_SQL_file import *
from __file_names import plotFile


#get_quotes_from_table(Open)
#get_quotes_from_table(High)
#get_quotes_from_table(Low)
(indices, dates, bull_1x_prices, bear_1x_prices,
 bull_3x_prices, bear_3x_prices) = rationalize_quotes_from_table(Close)
db.close()

output_file(plotFile)

p = figure(plot_width=800, plot_height=400)

p.line(x=indices, y=bull_1x_prices)
#p.line(x=dates, y=bear_1x_prices, line_color='blue')
#p.line(x=dates, y=bull_3x_prices, line_color='green')
#p.line(x=dates, y=bear_3x_prices, line_color='red')

#hover = HoverTool(
#    tooltips=[
#    ("(x,y)", "('@x{%F}', '$@{y}{%0.2f}')"),
#    ],
#    formatters={
#        'x' : 'datetime',   # use 'datetime' formatter for 'date' field
#        'y' : 'printf',     # use 'printf' formatter for 'adj close' field
#                            # use default 'numeral' formatter for other fields
#    },
#)

#p.multi_line(
#    xs=[dates, dates, dates, dates],
#    ys=[bull_1x_prices, bear_1x_prices, bull_3x_prices, bear_3x_prices],
#    line_color=['black', 'blue', 'green', 'red'],
#    )

show(p)
