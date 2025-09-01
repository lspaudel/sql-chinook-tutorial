# Calculating averages with AVG


Use the `AVG` function to compute the mean value of a numeric
column. Here we determine the average track price.


```sql

SELECT AVG(UnitPrice) AS AveragePrice FROM tracks;

```

**Sample result (first few rows):**

| AveragePrice |
| --- |
| 1.0508050242648312 |