## Explore US baby names

The US government releases name counts for Social Security number applicants ([details](https://www.ssa.gov/oact/babynames/background.html)). These data track the distribution of baby names in the US. Data from 1880-2014 are available for [download as a SQLite database](https://www.kaggle.com/kaggle/us-baby-names/downloads/database.sqlite.zip).

The namePlt function here in R and Python take a (case-insensitive) name string as input and return counts for the name over time separately for males and females. A data frame and plot of the name by year is returned. e.g. for my name:

```python
bdf = namePlt("bradley")
```

<img src="bp.jpeg" width="800" height="550"/>

The nameVars Python function gets name variants by fuzzy matching using Levenshtein Distance ([fuzzy wuzzy](https://github.com/seatgeek/fuzzywuzzy)). This function returns name variants, similarity to the entered name, gender, the year in which the variant reached its maximum, the count for that maximum year, and the total count of the variant in the data set.

```python
nameVars(df, "Bradley", numMatch = 10)

        Name  Sim Gender  max_year  max_year_count  total_count
0    Bradley  100      F      1984              56         1385
1    Bradley  100      M      1980            7216       298007
2   Brandley   93      M      1986               9           67
3     Bradly   92      F      1990               6           11
4     Bradly   92      M      1990             254         9104
5     Radley   92      F      2012               7           24
6     Radley   92      M      2014              77          792
7     Bradey   92      F      2007               9            9
8     Bradey   92      M      2002              39          694
9     Braley   92      F      2011              24          228
10    Braley   92      M      2007               6           11
11      Brad   90      F      1976              16          233
12      Brad   90      M      1960            2653        82631
13        Le   90      F      1982              35          877
14        Le   90      M      1990              19          775
15        Ad   90      M      1914               7           73
16       Rad   90      M      1963               9          116

```