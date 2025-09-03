# Working with hierarchical data using recursive CTEs


Recursive CTEs allow you to query hierarchical relationships,
such as an organizational chart. In the Chinook employees table,
the `ReportsTo` column references a manager. This query builds
a hierarchy starting from the top-level manager and recursively
traverses subordinate employees. The result shows each
employee alongside their manager chain. Not all SQLite
environments support recursive CTEs; if not supported, this
example may not execute. Results are limited for readability.


```sql

WITH RECURSIVE employee_hierarchy AS (
                -- Anchor member: select top-level employees (no manager)
                SELECT EmployeeId, FirstName || ' ' || LastName AS Name,
                       ReportsTo, 0 AS Level,
                       CAST(FirstName || ' ' || LastName AS TEXT) AS Path
                  FROM employees
                 WHERE ReportsTo IS NULL

                UNION ALL

                -- Recursive member: select employees reporting to the
                -- previous level
                SELECT e.EmployeeId, e.FirstName || ' ' || e.LastName AS Name,
                       e.ReportsTo, h.Level + 1 AS Level,
                       CAST(h.Path || ' -> ' || e.FirstName || ' ' || e.LastName AS TEXT) AS Path
                  FROM employees e
                  JOIN employee_hierarchy h ON e.ReportsTo = h.EmployeeId
            )
            SELECT EmployeeId, Name, Level, Path FROM employee_hierarchy ORDER BY Level, Name LIMIT 20;

```

**Sample result (first few rows):**

| EmployeeId | Name | Level | Path |
| --- | --- | --- | --- |
| 1 | Andrew Adams | 0 | Andrew Adams |
| 6 | Michael Mitchell | 1 | Andrew Adams -> Michael Mitchell |
| 2 | Nancy Edwards | 1 | Andrew Adams -> Nancy Edwards |
| 3 | Jane Peacock | 2 | Andrew Adams -> Nancy Edwards -> Jane Peacock |
| 8 | Laura Callahan | 2 | Andrew Adams -> Michael Mitchell -> Laura Callahan |