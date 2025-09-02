# Simplifying queries with common table expressions (CTE)


A CTE is a named temporary result set defined within a query.
This example uses a simple CTE to select the top five invoices by
total amount. The CTE improves readability by separating the
logic for selecting the top invoices from the outer query.


```sql

WITH TopInvoices AS (SELECT InvoiceId, Total FROM invoices ORDER BY Total DESC LIMIT 5) SELECT * FROM TopInvoices ORDER BY Total DESC;

```

**Sample result (first few rows):**

| InvoiceId | Total |
| --- | --- |
| 404.0 | 25.86 |
| 299.0 | 23.86 |
| 96.0 | 21.86 |
| 194.0 | 21.86 |
| 89.0 | 18.86 |