"""
This file has imports and uses functions for retrieving data from the SQLite
file and then visualizing that data

Key to naming conventions:
camelCase      global (and imported) variables and function parameters
CamelCase      class names
snake_case     variables not intended to be used globally and function names
"""


from bokeh.plotting import figure, output_file, show
from bokeh.models import BoxZoomTool, HoverTool, PanTool, ResetTool, SaveTool
from _2_port_data_to_from_SQL_file import *
from __file_names import plotFile


#(indices, dates, bull_1x_prices, bear_1x_prices,
# bull_3x_prices, bear_3x_prices) = rationalize_quotes_from_table(Open)
#(indices, dates, bull_1x_prices, bear_1x_prices,
# bull_3x_prices, bear_3x_prices) = rationalize_quotes_from_table(High)
#(indices, dates, bull_1x_prices, bear_1x_prices,
# bull_3x_prices, bear_3x_prices) = rationalize_quotes_from_table(Low)
(indices, dates, bull_1x_prices, bear_1x_prices,
 bull_3x_prices, bear_3x_prices) = rationalize_quotes_from_table(Close)
db.close()

output_file(plotFile)

hover = HoverTool( tooltips=[('close value', '$y{$ 0.00}')] )

TOOLS = [ hover, BoxZoomTool(), PanTool(), SaveTool(), ResetTool() ]

p = figure(title='Comparisons of ETF performance from ' + plotFile,
           plot_width=1200, plot_height=600,
           x_axis_label='close date', y_axis_label='value of $10000 investment (log scale)',
           x_axis_type='datetime', y_axis_type='log',
           tools=TOOLS)

p.line(x=dates, y=bull_1x_prices, line_color='black', legend='non-leveraged long')
p.line(x=dates, y=bear_1x_prices, line_color='blue', legend='non-leveraged short')
p.line(x=dates, y=bull_3x_prices, line_color='green', legend='3x leveraged long')
p.line(x=dates, y=bear_3x_prices, line_color='red', legend='3x leveraged short')

p.legend.location = 'bottom_left'

show(p)
