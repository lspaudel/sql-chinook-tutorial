# Including duplicates with UNION ALL


`UNION ALL` also combines results from two queries but keeps
duplicates. This query returns the list of countries from the
customers table twice, so countries with more customers will appear
multiple times.


```sql

SELECT Country FROM customers UNION ALL SELECT Country FROM customers ORDER BY Country LIMIT 20;

```

**Sample result (first few rows):**

| Country |
| --- |
| Argentina |
| Argentina |
| Australia |
| Australia |
| Austria |