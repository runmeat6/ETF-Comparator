# ETF Comparator
## Question
What do performance charts look like over time between related ETFs?
## Restated problem
Analyze related exchange traded funds against one another, namely:
long and short non-leveraged and their 3x margin leveraged counterparts.
(Disclaimer note: leveraged funds are not recommended for long term use.)
## Data source
A Kaggle gzip file from which four files were extracted based on correlation between them of being exactly what was wanted (and there were only four sets of four correlated files, because there are few non-leveraged short stock funds -- the other three being SP400_mid_cap, Russell2000_small_cap, and Nasdaq_composite, whereas SP500_large_cap was chosen for demonstration).
## Getting started
Files (and directory) which are required from the repository:
   * SP500_large_cap_wrapper.py
   * general_wrapper.py
   * _0_read_data.py
   * _1_filter_data.py
   * _2_port_data_to_from_SQL_file.py
   * _3_visualize_data.py
   * SP500_large_cap/
   * SP500_large_cap/spy.us.txt
   * SP500_large_cap/sh.us.txt
   * SP500_large_cap/upro.us.txt
   * SP500_large_cap/spxu.us.txt
Necessary non-standard libraries available via PyPI using pip install:
   * peewee
   * bokeh
Files clobbered during script execution:
   * __file_names.py
   * SP500_large_cap.sql

Note: bokeh needs content delivery network access, so an active connection with internet access is required.

Use SP500_large_cap_wrapper.py to begin execution. It clobbers __file_names.py writing all the names of the files that will need to be known by the other scripts and deletes SP500_large_cap.sql if it exists. Finally, it imports general_wrapper.py which is the true wrapper file -- SP500_large_cap_wrapper.py being more of a set-up file than a wrapper file. Anyhow, general_wrapper.py imports _0_read_data.py which allows it to read the four data files found in the SP500_large_cap directory. Then it imports _1_filter_data.py to make all the data the same length by filtering based on matching the intersecting set of dates amongst them. Next it imports _2_port_data_to_from_SQL_file.py to export the filtered data into tables based on the four price columns: open, high, low, and close. Thus, the data is transformed from being separate funds with price type columns to being separate price types with ETF columns -- in each case, date remains the primary key (but, peewee does not play well with non-integer primary keys, so it has been allowed to include auto-increment identifiers). Next only the "close" table data is read in for visualization of the four plots on a single logarithmic scale y-axis and datetime x-axis graph representing the closing prices of each of the exchange traded funds over time (starting with a hypothetical initial $10^4=$10000 investment). That is accomplished with the import of _3_visualize_data.
## Further notes
SP500_large_cap_wrapper.py was used versus hard-coding the directory and files, because there was an original intention to do the other three data sets heretofore mentioned; nevertheless, it seemed like good practice to stay flexible. There are no conclusions per se, but the plot looked pretty. Further study of trough/peak and other ranged conditions would be interesting. Usage of Bokeh ColumnDataSource would have allowed dates to be displayed in the hovertool, but time became elusive, so only 'close value' made sense to show. (A warning may appear that Bokeh is using something deprecated from Pandas library, which would be the propagation of a Bokeh problem.)
## Full list of libraries installed
   * alabaster (0.7.10)
   * Babel (2.5.3)
   * bleach (2.1.2)
   * bokeh (0.12.5)
   * certifi (2018.1.18)
   * chardet (3.0.4)
   * colorama (0.3.9)
   * cycler (0.10.0)
   * decorator (4.1.2)
   * docutils (0.14)
   * entrypoints (0.2.3)
   * html5lib (1.0.1)
   * idna (2.5)
   * imagesize (0.7.1)
   * ipykernel (4.7.0)
   * ipython (6.2.1)
   * ipython-genutils (0.2.0)
   * ipywidgets (7.1.0)
   * jedi (0.11.1)
   * Jinja2 (2.10)
   * jsonschema (2.6.0)
   * jupyter (1.0.0)
   * jupyter-client (5.2.1)
   * jupyter-console (5.2.0)
   * jupyter-core (4.4.0)
   * MarkupSafe (1.0)
   * matplotlib (2.1.2)
   * mistune (0.8.3)
   * nbconvert (5.3.1)
   * nbformat (4.4.0)
   * notebook (5.2.2)
   * numpy (1.12.1)
   * numpydoc (0.7.0)
   * pandas (0.20.1)
   * pandocfilters (1.4.2)
   * parso (0.1.1)
   * peewee (3.0.2)
   * pickleshare (0.7.4)
   * pip (9.0.1)
   * prompt-toolkit (1.0.15)
   * Pygments (2.2.0)
   * pyparsing (2.2.0)
   * python-dateutil (2.6.1)
   * pytz (2017.3)
   * PyYAML (3.12)
   * pyzmq (16.0.3)
   * qtconsole (4.3.1)
   * requests (2.17.3)
   * setuptools (28.8.0)
   * simplegeneric (0.8.1)
   * six (1.11.0)
   * snowballstemmer (1.2.1)
   * Sphinx (1.6.6)
   * sphinxcontrib-websupport (1.0.1)
   * testpath (0.3.1)
   * tornado (4.5.3)
   * traitlets (4.3.2)
   * urllib3 (1.21.1)
   * wcwidth (0.1.7)
   * webencodings (0.5.1)
   * widgetsnbextension (3.1.0)
## Authors
   * **Bryan Alexander**
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
