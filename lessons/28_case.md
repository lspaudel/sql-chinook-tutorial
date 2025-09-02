# Adding conditional logic with CASE


The `CASE` expression returns a value based on conditional
logic. This query labels tracks as 'Expensive' if the price is
greater than $1.00 and 'Cheap' otherwise. Labels can be used in
result sets just like any other computed column.


```sql

SELECT Name, UnitPrice, CASE WHEN UnitPrice > 1.00 THEN 'Expensive' ELSE 'Cheap' END AS PriceCategory FROM tracks ORDER BY UnitPrice DESC LIMIT 10;

```

**Sample result (first few rows):**

| Name | UnitPrice | PriceCategory |
| --- | --- | --- |
| Battlestar Galactica: The Story So Far | 1.99 | Expensive |
| Occupation / Precipice | 1.99 | Expensive |
| Exodus, Pt. 1 | 1.99 | Expensive |
| Exodus, Pt. 2 | 1.99 | Expensive |
| Collaborators | 1.99 | Expensive |