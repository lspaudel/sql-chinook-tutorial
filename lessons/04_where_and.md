# Combining conditions with AND


You can combine multiple conditions using the `AND` operator. This
query finds customers in the USA who are also located in
California. Both conditions must be true for a row to be included.


```sql

SELECT * FROM customers WHERE Country = 'USA' AND State = 'CA';

```

**Sample result (first few rows):**

| CustomerId | FirstName | LastName | Company | Address | City | State | Country | PostalCode | Phone | Fax | Email | SupportRepId |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | Frank | Harris | Google Inc. | 1600 Amphitheatre Parkway | Mountain View | CA | USA | 94043-1351 | +1 (650) 253-0000 | +1 (650) 253-0000 | fharris@google.com | 4 |
| 19 | Tim | Goyer | Apple Inc. | 1 Infinite Loop | Cupertino | CA | USA | 95014 | +1 (408) 996-1010 | +1 (408) 996-1011 | tgoyer@apple.com | 3 |
| 20 | Dan | Miller | None | 541 Del Medio Avenue | Mountain View | CA | USA | 94040-111 | +1 (650) 644-3358 | None | dmiller@comcast.com | 4 |