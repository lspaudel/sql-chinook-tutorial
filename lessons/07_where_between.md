# Filtering by range with BETWEEN


Use `BETWEEN` to filter numeric values within a specified range.
Here we select tracks priced between $0.99 and $1.99 inclusive. The
`UnitPrice` column stores the price of each track.


```sql

SELECT Name, UnitPrice FROM tracks WHERE UnitPrice BETWEEN 0.99 AND 1.99;

```

**Sample result (first few rows):**

| Name | UnitPrice |
| --- | --- |
| For Those About To Rock (We Salute You) | 0.99 |
| Balls to the Wall | 0.99 |
| Fast As a Shark | 0.99 |
| Restless and Wild | 0.99 |
| Princess of the Dawn | 0.99 |