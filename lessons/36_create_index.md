# Improving performance with indexes


An index speeds up lookups on a table column. Creating too many
indexes can slow down writes, so it’s important to index only
where needed. This example creates an index on the `AlbumId`
column of the `tracks` table to improve joins and lookups by
album. (This statement is not executed automatically.)


```sql

CREATE INDEX idx_tracks_albumid ON tracks (AlbumId);

```