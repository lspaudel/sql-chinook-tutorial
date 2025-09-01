# Descending order sorting


Add the `DESC` keyword after a column name to sort in descending
order. Here we list the five most expensive tracks first by
ordering on `UnitPrice` descending.


```sql

SELECT Name, UnitPrice FROM tracks ORDER BY UnitPrice DESC LIMIT 5;

```

**Sample result (first few rows):**

| Name | UnitPrice |
| --- | --- |
| Battlestar Galactica: The Story So Far | 1.99 |
| Occupation / Precipice | 1.99 |
| Exodus, Pt. 1 | 1.99 |
| Exodus, Pt. 2 | 1.99 |
| Collaborators | 1.99 |