# Testing membership with IN


The `IN` operator checks whether a value matches any value in a
list. This query selects all genres whose name is either 'Rock' or
'Jazz'.


```sql

SELECT * FROM genres WHERE Name IN ('Rock', 'Jazz');

```

**Sample result (first few rows):**

| GenreId | Name |
| --- | --- |
| 1 | Rock |
| 2 | Jazz |