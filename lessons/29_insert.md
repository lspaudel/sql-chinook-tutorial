# Inserting rows into a table


`INSERT` adds new rows to a table. In practice you would insert
data into existing business tables, but here we create a simple
temporary table to demonstrate. Create the table, insert a row,
and query the contents to see the result. (These statements are
not executed automatically by this tutorial.)


```sql

-- Create a temporary table for demonstration
            CREATE TABLE IF NOT EXISTS demo_insert (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT
            );

            -- Insert a new row
            INSERT INTO demo_insert (Name) VALUES ('Example Row');

            -- Query the table to see the inserted row
            SELECT * FROM demo_insert;

```