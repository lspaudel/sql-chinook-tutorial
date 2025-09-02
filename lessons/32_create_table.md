# Creating new tables


The `CREATE TABLE` statement defines a new table. Here we create
a simple table called `example_table` with an integer primary key
and a text column. You would normally run this once during
database setup. (This statement is not executed automatically.)


```sql

CREATE TABLE example_table (
                Id INTEGER PRIMARY KEY,
                Description TEXT
            );

```