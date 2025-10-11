# SQL Tutorial with the Chinook Database

This repository is a hands‑on tutorial designed to take you from SQL
beginner to advanced concepts. It uses the **Chinook** sample
database, a digital media store schema that includes tables for
artists, albums, media tracks, invoices, customers and more.  The
database contains eleven tables in total: employees, customers,
invoices and invoice items, artists, albums, media types, genres,
tracks, playlists and the playlist–track mapping.  The
data was assembled from a mixture of sources: media data comes from
real iTunes library metadata, customer and employee data uses fictitious
names and addresses, and sales data is randomly generated over a four‑year
period.

## What’s included?

* `chinook.db` — A SQLite copy of the Chinook database.  You can
  explore it using the `sqlite3` command‑line tool or any SQL client
  that understands SQLite.  For example, open a terminal and run:

  ```sh
  sqlite3 chinook.db
  sqlite> .tables
  sqlite> SELECT * FROM albums LIMIT 5;
  ```

  If you prefer Python, you can use the built‑in `sqlite3` module or
  `pandas` to query the database.

* `lessons/` — A folder containing forty Markdown files.  Each file
  covers one SQL concept in a conversational style and provides a
  sample query against the Chinook data.  When appropriate, the
  generated lesson includes a table of sample results so you can see
  what the query returns.

## How to use this tutorial

1. Clone or download this repository.
2. Open the `lessons` directory and work through the files in numeric
   order (`01_select_basic.md`, `02_select_columns.md`, …).  Each
   lesson contains a short explanation, the SQL query, and a sample
   result for you to inspect.
3. Run the queries against `chinook.db` using your preferred SQL
   client to experiment and modify them.  Feel free to explore by
   changing filter values, adding conditions or creating your own
   queries.

### Notes on data‑modifying examples

Some later lessons demonstrate `INSERT`, `UPDATE`, `DELETE` and other
data definition or manipulation statements.  To avoid changing the
sample data, these queries are provided as examples and are **not
executed** by the lesson generator.  When you try them yourself, you
may want to create temporary tables or wrap your statements in
transactions and roll back, so the original dataset remains intact.

## Contributing

This project is intended as a starting point for learning SQL.  If you
find an error or have suggestions for new lessons, please feel free to
open an issue or submit a pull request.  Contributions that improve
clarity, fix mistakes or extend the coverage of SQL topics are very
welcome.
