# Finding common values with INTERSECT


The `INTERSECT` operator returns rows that are common to both
queries. This query finds countries that appear in both the
customers and employees tables.


```sql

SELECT Country FROM customers INTERSECT SELECT Country FROM employees ORDER BY Country;

```

**Sample result (first few rows):**

| Country |
| --- |
| Canada |