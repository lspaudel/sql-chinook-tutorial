# Deleting rows


Use `DELETE` to remove rows from a table. Continuing with the
`demo_insert` table, delete the row we previously inserted and
then select from the table to confirm it's empty. (These
statements are illustrative and not executed automatically.)


```sql

-- Delete the row from the demo_insert table
            DELETE FROM demo_insert WHERE Id = 1;

            -- Query the table to confirm deletion
            SELECT * FROM demo_insert;

```