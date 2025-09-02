# Combining tables with INNER JOIN


Joins combine rows from two or more tables based on related columns.
An `INNER JOIN` returns only rows that have matching values on
both sides. Here we join `albums` with `artists` to show each
album's title alongside the artist's name.


```sql

SELECT albums.Title AS Album, artists.Name AS Artist FROM albums JOIN artists ON albums.ArtistId = artists.ArtistId ORDER BY Artist, Album LIMIT 10;

```

**Sample result (first few rows):**

| Album | Artist |
| --- | --- |
| For Those About To Rock We Salute You | AC/DC |
| Let There Be Rock | AC/DC |
| A Copland Celebration, Vol. I | Aaron Copland & London Symphony Orchestra |
| Worlds | Aaron Goldberg |
| The World of Classical Favourites | Academy of St. Martin in the Fields & Sir Neville Marriner |