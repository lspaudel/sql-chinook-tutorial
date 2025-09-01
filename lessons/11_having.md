# Filtering groups with HAVING


After grouping rows, use the `HAVING` clause to filter the
aggregated results. This query shows countries with more than five
customers.


```sql

SELECT Country, COUNT(*) AS CustomerCount FROM customers GROUP BY Country HAVING COUNT(*) > 5 ORDER BY CustomerCount DESC;

```

**Sample result (first few rows):**

| Country | CustomerCount |
| --- | --- |
| USA | 13 |
| Canada | 8 |