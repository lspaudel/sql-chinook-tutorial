# SQL Tutorial with the Chinook Database

This repository is a hands‑on tutorial designed to take you from SQL beginner to advanced concepts. It uses the **Chinook** sample
database — a realistic dataset that models a digital media store (similar to iTunes). It includes tables for artists, albums, tracks, customers, invoices, and more, making it perfect for practicing queries, joins, aggregations, and subqueries.

---

## 🗃️ About the Chinook Database

The **Chinook Sample Database** is a public, open-source example database created by Microsoft developer Lynn Root.  
It is widely used in tutorials and courses.

Each table in the database stores realistic information related to music sales:
- **albums** – album titles and associated artists  
- **artists** – artist information  
- **tracks** – individual music tracks with album, genre, and media type  
- **genres** – list of available music genres  
- **customers** – customer contact and location details  
- **invoices** – customer invoices  
- **invoice_items** – items included in each invoice  
- **playlists** – playlists created by users  
- **playlist_track** – mapping between playlists and tracks  
- **employees** – employee and support representative data  

---

## 📥 How to Get the Database

You can download the SQLite version of the Chinook database directly from the official GitHub repository.

### Option 1: Download via Browser
1. Go to the official Chinook Database repo:  
   🔗 [https://github.com/lerocha/chinook-database](https://github.com/lerocha/chinook-database)
2. Open the folder: `ChinookDatabase/DataSources/`
3. Download the file: **`Chinook_Sqlite.sqlite`**
4. Rename it to **`chinook.db`**
5. Place it inside this project folder.

### Option 2: Download via Command Line
If you prefer to download directly from the terminal:

```bash
# Using wget
wget https://github.com/lerocha/chinook-database/raw/master/Chinook_Sqlite.sqlite -O chinook.db

# Or using curl
curl -L -o chinook.db https://github.com/lerocha/chinook-database/raw/master/Chinook_Sqlite.sqlite
```
### Option 3: Use the `chinook.db` database provided within this project.
 You can explore it using the `sqlite3` command‑line tool or any SQL client that understands SQLite.  For example, open a terminal and run:

  ```sh
  sqlite3 chinook.db
  sqlite> .tables
  sqlite> SELECT * FROM albums LIMIT 5;
  ```

  If you prefer Python, you can use the built‑in `sqlite3` module or
  `pandas` to query the database. An example code `panda_query.ipynb` is also provided to get started.

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
find an error or have suggestions for new lessons, please feel free to contribute.  
Contributions that improve clarity, fix mistakes or extend the coverage of SQL topics are very welcome.
