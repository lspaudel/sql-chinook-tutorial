# Referencing a table to itself with SELF JOIN


A self join is a join of a table with itself. It's useful for
hierarchical relationships stored in a single table. In the
employees table, the `ReportsTo` column refers to the manager of
each employee. This query pairs employees with their managers.


```sql

SELECT e.FirstName || ' ' || e.LastName AS Employee, m.FirstName || ' ' || m.LastName AS Manager FROM employees e LEFT JOIN employees m ON e.ReportsTo = m.EmployeeId ORDER BY Employee LIMIT 10;

```

**Sample result (first few rows):**

| Employee | Manager |
| --- | --- |
| Andrew Adams | None |
| Jane Peacock | Nancy Edwards |
| Laura Callahan | Michael Mitchell |
| Margaret Park | Nancy Edwards |
| Michael Mitchell | Andrew Adams |