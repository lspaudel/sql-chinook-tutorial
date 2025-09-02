# Using window functions


Window functions perform calculations across sets of rows that
relate to the current row. The `ROW_NUMBER()` function assigns
a unique sequential integer to rows ordered by price. This query
ranks tracks by descending price.


```sql

SELECT TrackId, Name, UnitPrice, ROW_NUMBER() OVER (ORDER BY UnitPrice DESC) AS PriceRank FROM tracks ORDER BY UnitPrice DESC LIMIT 10;

```

**Sample result (first few rows):**

| TrackId | Name | UnitPrice | PriceRank |
| --- | --- | --- | --- |
| 2819 | Battlestar Galactica: The Story So Far | 1.99 | 1 |
| 2820 | Occupation / Precipice | 1.99 | 2 |
| 2821 | Exodus, Pt. 1 | 1.99 | 3 |
| 2822 | Exodus, Pt. 2 | 1.99 | 4 |
| 2823 | Collaborators | 1.99 | 5 |