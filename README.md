
# ETF Comparator
## Question
What do performance charts look like over time between related ETFs?
## Restated problem
Analyze related exchange traded funds against one another, namely:
long and short non-leveraged and their 3x margin leveraged counterparts.
(Disclaimer note: leveraged funds are not recommended for long term use.)
## Data sources
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
SP500_large_cap_wrapper.py was used versus hard-coding the directory and files, because there was an original intention to do the other three data sets heretofore mentioned; nevertheless, it seemed like good practice to stay flexible. There are no conclusions per se, but the plot looked pretty. Further study of trough/peak and other ranged conditions would be interesting.
## Authors
   * **Bryan Alexander**
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
