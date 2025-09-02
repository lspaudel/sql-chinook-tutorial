# Changing a table with ALTER TABLE


Use `ALTER TABLE` to modify an existing table structure. In this
example we add a `CreatedAt` column to the `example_table` to
record when each row was created. (This statement is not
executed automatically.)


```sql

ALTER TABLE example_table ADD COLUMN CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP;

```