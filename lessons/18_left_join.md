# Including unmatched rows with LEFT JOIN


A `LEFT JOIN` (or left outer join) returns all rows from the left
table and the matching rows from the right table. If there is no
match, the result contains NULLs for the right table's columns.
This query lists customers and their invoices, if any. Customers
without invoices still appear in the result.


```sql

SELECT customers.FirstName || ' ' || customers.LastName AS Customer, invoices.InvoiceId, invoices.Total FROM customers LEFT JOIN invoices ON customers.CustomerId = invoices.CustomerId ORDER BY Customer LIMIT 10;

```

**Sample result (first few rows):**

| Customer | InvoiceId | Total |
| --- | --- | --- |
| Aaron Mitchell | 50 | 1.98 |
| Aaron Mitchell | 61 | 13.86 |
| Aaron Mitchell | 116 | 8.91 |
| Aaron Mitchell | 245 | 1.98 |
| Aaron Mitchell | 268 | 3.96 |