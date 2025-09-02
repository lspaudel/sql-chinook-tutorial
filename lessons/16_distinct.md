# Removing duplicates with DISTINCT


The `DISTINCT` keyword removes duplicate values from the result set.
This query lists all unique countries where customers reside.


```sql

SELECT DISTINCT Country FROM customers ORDER BY Country;

```

**Sample result (first few rows):**

| Country |
| --- |
| Argentina |
| Australia |
| Austria |
| Belgium |
| Brazil |