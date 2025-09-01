# Finding minimum and maximum values


The `MIN` and `MAX` functions return the smallest and largest
values in a column. This example shows the cheapest and most
expensive track prices.


```sql

SELECT MIN(UnitPrice) AS MinPrice, MAX(UnitPrice) AS MaxPrice FROM tracks;

```

**Sample result (first few rows):**

| MinPrice | MaxPrice |
| --- | --- |
| 0.99 | 1.99 |