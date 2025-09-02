# Finding differences with EXCEPT


The `EXCEPT` operator returns rows from the first query that are
not present in the second. This example lists countries that have
customers but no employees. Note that the country names are
compared across the two tables.


```sql

SELECT Country FROM customers EXCEPT SELECT Country FROM employees ORDER BY Country;

```

**Sample result (first few rows):**

| Country |
| --- |
| Argentina |
| Australia |
| Austria |
| Belgium |
| Brazil |