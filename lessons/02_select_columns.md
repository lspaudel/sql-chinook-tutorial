# Selecting specific columns


Instead of selecting every column, you can specify exactly which
columns you want to see. Here we select the `FirstName` and
`LastName` columns from the `employees` table to list the staff
names without showing their contact details or other fields.


```sql

SELECT FirstName, LastName FROM employees;

```

**Sample result (first few rows):**

| FirstName | LastName |
| --- | --- |
| Andrew | Adams |
| Nancy | Edwards |
| Jane | Peacock |
| Margaret | Park |
| Steve | Johnson |