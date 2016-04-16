## Explore US baby names

The US government releases name counts for Social Security number applicants ([details](https://www.ssa.gov/oact/babynames/background.html)). These data track the distribution of baby names in the US. Data from 1880-2014 are available for [download as a SQLite database](https://www.kaggle.com/kaggle/us-baby-names/downloads/database.sqlite.zip).

namePlt function here in R and Python take a (case-insensitive) name string as input and return counts for the name over time separately for males and females. A data frame and plot of the name by year is returned. e.g. for my name:

```python
bdf = namePlt("bradley")
```

<img src="bp.jpeg" width="800" height="550"/>

nameVars function gets name variants by fuzzy matching using Levenshtein Distance ([fuzzy wuzzy](https://github.com/seatgeek/fuzzywuzzy)).

```python
nameVars(df, "Bradley", numMatch = 10)

        Name  sim Gender   Count
0    Bradley  100      F    1385
1    Bradley  100      M  298007
2   Brandley   93      M      67
3     Bradly   92      F      11
4     Bradly   92      M    9104
5     Radley   92      F      24
6     Radley   92      M     792
7     Bradey   92      F       9
8     Bradey   92      M     694
9     Braley   92      F     228
10    Braley   92      M      11
11      Brad   90      F     233
12      Brad   90      M   82631
13        Le   90      F     877
14        Le   90      M     775
15        Ad   90      M      73
16       Rad   90      M     116
```