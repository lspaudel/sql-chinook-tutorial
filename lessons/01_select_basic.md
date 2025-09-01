# Basic SELECT – retrieve all columns


The `SELECT` statement is the foundation of querying in SQL. A
basic `SELECT` retrieves all columns and rows from a table. In the
Chinook database, the `artists` table stores information about
musical artists. This query returns the first five artists and
shows every column in the table.


```sql

SELECT * FROM artists LIMIT 5;

```

**Sample result (first few rows):**

| ArtistId | Name |
| --- | --- |
| 1 | AC/DC |
| 2 | Accept |
| 3 | Aerosmith |
| 4 | Alanis Morissette |
| 5 | Alice In Chains |