# Removing tables with DROP TABLE


When a table is no longer needed, `DROP TABLE` permanently
removes it and its data. Here we drop the `example_table` we
created in previous lessons. (This statement is not executed
automatically.)


```sql

DROP TABLE IF EXISTS example_table;

```