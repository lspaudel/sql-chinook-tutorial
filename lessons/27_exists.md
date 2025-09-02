# Checking for existence with EXISTS


The `EXISTS` operator tests whether a subquery returns any rows. In
this query we list artists who have at least one album in the
database. The subquery checks for the existence of albums linked
to each artist.


```sql

SELECT Name FROM artists a WHERE EXISTS (SELECT 1 FROM albums al WHERE al.ArtistId = a.ArtistId) ORDER BY Name LIMIT 10;

```

**Sample result (first few rows):**

| Name |
| --- |
| AC/DC |
| Aaron Copland & London Symphony Orchestra |
| Aaron Goldberg |
| Academy of St. Martin in the Fields & Sir Neville Marriner |
| Academy of St. Martin in the Fields Chamber Ensemble & Sir Neville Marriner |