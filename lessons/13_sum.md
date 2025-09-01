# Summing values with SUM


The `SUM` function adds up all values of a numeric column. This
query calculates the total of all invoice amounts.


```sql

SELECT SUM(Total) AS TotalRevenue FROM invoices;

```

**Sample result (first few rows):**

| TotalRevenue |
| --- |
| 2328.600000000004 |