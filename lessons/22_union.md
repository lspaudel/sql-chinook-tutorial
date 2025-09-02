# Combining result sets with UNION


The `UNION` operator combines the results of two queries and
eliminates duplicate rows. Here we list all unique countries that
appear in either the customers or employees tables. Each country
appears only once in the final set.


```sql

SELECT Country FROM customers UNION SELECT Country FROM employees ORDER BY Country;

```

**Sample result (first few rows):**

| Country |
| --- |
| Argentina |
| Australia |
| Austria |
| Belgium |
| Brazil |