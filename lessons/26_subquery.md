# Using subqueries for comparisons


A subquery is a query nested within another query. In this
example we select tracks whose price is above the average track
price. The subquery computes the average price across all tracks.


```sql

SELECT Name, UnitPrice FROM tracks WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM tracks) ORDER BY UnitPrice DESC LIMIT 10;

```

**Sample result (first few rows):**

| Name | UnitPrice |
| --- | --- |
| Battlestar Galactica: The Story So Far | 1.99 |
| Occupation / Precipice | 1.99 |
| Exodus, Pt. 1 | 1.99 |
| Exodus, Pt. 2 | 1.99 |
| Collaborators | 1.99 |