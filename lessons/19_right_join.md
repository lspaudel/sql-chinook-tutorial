# Simulating a RIGHT JOIN in SQLite


SQLite does not support the `RIGHT JOIN` syntax, but you can achieve
the same effect by swapping the tables and using a `LEFT JOIN`.
This query finds invoices and their customers, including invoices
that might not have a matching customer (although in this
database every invoice has a valid customer). The principle is
explained rather than demonstrated with missing data.


```sql

SELECT invoices.InvoiceId, customers.FirstName || ' ' || customers.LastName AS Customer, invoices.Total FROM invoices LEFT JOIN customers ON customers.CustomerId = invoices.CustomerId LIMIT 10;

```

**Sample result (first few rows):**

| InvoiceId | Customer | Total |
| --- | --- | --- |
| 1 | Leonie Köhler | 1.98 |
| 2 | Bjørn Hansen | 3.96 |
| 3 | Daan Peeters | 5.94 |
| 4 | Mark Philips | 8.91 |
| 5 | John Gordon | 13.86 |