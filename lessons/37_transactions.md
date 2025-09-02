# Ensuring atomicity with transactions


A transaction groups multiple statements into a single unit of
work. If any statement fails, the entire transaction can be
rolled back. This example shows how to begin a transaction,
update a record, and then roll back the change. (These
statements are illustrative and not executed automatically.)


```sql

-- Start a transaction
            BEGIN TRANSACTION;

            -- Example update: increase the price of a specific track
            UPDATE tracks SET UnitPrice = UnitPrice + 0.10 WHERE TrackId = 1;

            -- Roll back the change
            ROLLBACK;

```