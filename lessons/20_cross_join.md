# Creating a Cartesian product with CROSS JOIN


A `CROSS JOIN` returns the Cartesian product of two tables, meaning
each row of the first table is paired with each row of the second.
This can quickly produce large result sets. Here we cross join
employees and media types and show only a few rows to illustrate
the pattern.


```sql

SELECT employees.FirstName || ' ' || employees.LastName AS Employee, media_types.Name AS MediaType FROM employees CROSS JOIN media_types LIMIT 10;

```

**Sample result (first few rows):**

| Employee | MediaType |
| --- | --- |
| Andrew Adams | MPEG audio file |
| Andrew Adams | Protected AAC audio file |
| Andrew Adams | Protected MPEG-4 video file |
| Andrew Adams | Purchased AAC audio file |
| Andrew Adams | AAC audio file |