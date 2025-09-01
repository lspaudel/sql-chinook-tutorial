# Filtering rows with WHERE


The `WHERE` clause filters rows based on a condition. In this
example we retrieve all customers from the United States. Only
rows where the `Country` column is `USA` are returned.


```sql

SELECT * FROM customers WHERE Country = 'USA';

```

**Sample result (first few rows):**

| CustomerId | FirstName | LastName | Company | Address | City | State | Country | PostalCode | Phone | Fax | Email | SupportRepId |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | Frank | Harris | Google Inc. | 1600 Amphitheatre Parkway | Mountain View | CA | USA | 94043-1351 | +1 (650) 253-0000 | +1 (650) 253-0000 | fharris@google.com | 4 |
| 17 | Jack | Smith | Microsoft Corporation | 1 Microsoft Way | Redmond | WA | USA | 98052-8300 | +1 (425) 882-8080 | +1 (425) 882-8081 | jacksmith@microsoft.com | 5 |
| 18 | Michelle | Brooks | None | 627 Broadway | New York | NY | USA | 10012-2612 | +1 (212) 221-3546 | +1 (212) 221-4679 | michelleb@aol.com | 3 |
| 19 | Tim | Goyer | Apple Inc. | 1 Infinite Loop | Cupertino | CA | USA | 95014 | +1 (408) 996-1010 | +1 (408) 996-1011 | tgoyer@apple.com | 3 |
| 20 | Dan | Miller | None | 541 Del Medio Avenue | Mountain View | CA | USA | 94040-111 | +1 (650) 644-3358 | None | dmiller@comcast.com | 4 |