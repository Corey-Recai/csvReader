# csvReader

## A csv reader that is supposed to mimic a few methods that the pandas library provides.

To use put it in the same folder as the file you are working on and import it into a blank python file like this:

```python
from csvReader import pycsv
```

Right now you can access your csv data using a new `pycsv()`object and then calling the `read_csv()` method on your object:
The `read_csv()` method takes the arguments `'columnHeaders'` and `'columnNames'`

```python
df = pycsv(file="filename.csv")
df.read_csv()
```

You can also use the `count()` method like this:
It takes the argument axis as either `'index'` or `'columns'`

```python
df.count(axis="index")
```

The `data()` method returns the csv as a dictionary:

```python
df.data()
```

The `_sum()` method takes a `'columnName'` argument and returns the sum of the column or the sum of each column:

```python
df.sum()
df.sum(columnName="columnName")
```

The `diff()` method take a `'columnName'` argument and returns the difference between each row in the column. Values can not be alphanumeric:

```python
df.diff(columnName="columnName")
```
