# Counting rows with COUNT


`COUNT(*)` returns the total number of rows in a table. Here we
count the number of tracks in the database.


```sql

SELECT COUNT(*) AS TrackCount FROM tracks;

```

**Sample result (first few rows):**

| TrackCount |
| --- |
| 3503 |