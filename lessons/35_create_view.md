# Creating reusable queries with VIEWs


A view is a saved query that can be treated like a table. This
example creates a view combining customer names and their invoice
totals. You can query the view just like a normal table. (The
creation statement is not executed automatically, but the
subsequent SELECT demonstrates how you would use it.)


```sql

-- Create the view
            CREATE VIEW IF NOT EXISTS customer_invoices AS
            SELECT c.FirstName || ' ' || c.LastName AS Customer,
                   i.Total
              FROM customers c
              JOIN invoices i ON c.CustomerId = i.CustomerId;

            -- Query the view
            SELECT * FROM customer_invoices ORDER BY Total DESC LIMIT 10;

```