# Updating existing rows


The `UPDATE` statement modifies existing rows. Using the same
temporary table from the previous lesson, change the row's name
and then retrieve it to verify the update. (These statements
are illustrative and not executed automatically.)


```sql

-- Update the row in the demo_insert table
            UPDATE demo_insert SET Name = 'Updated Row' WHERE Id = 1;

            -- Query the table to see the updated data
            SELECT * FROM demo_insert;

```