# Sorting results with ORDER BY


The `ORDER BY` clause sorts the result set. By default it sorts in
ascending order. This example lists employees by last name
alphabetically.


```sql

SELECT FirstName, LastName FROM employees ORDER BY LastName;

```

**Sample result (first few rows):**

| FirstName | LastName |
| --- | --- |
| Andrew | Adams |
| Laura | Callahan |
| Nancy | Edwards |
| Steve | Johnson |
| Robert | King |