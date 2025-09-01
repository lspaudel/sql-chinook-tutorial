# Grouping data with GROUP BY


The `GROUP BY` clause aggregates rows sharing the same value of
specified columns. This query counts how many customers are in
each country.


```sql

SELECT Country, COUNT(*) AS CustomerCount FROM customers GROUP BY Country ORDER BY CustomerCount DESC;

```

**Sample result (first few rows):**

| Country | CustomerCount |
| --- | --- |
| USA | 13 |
| Canada | 8 |
| France | 5 |
| Brazil | 5 |
| Germany | 4 |