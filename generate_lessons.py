"""
This script generates Markdown lesson files for a SQL tutorial project
using the Chinook sample database. Each lesson covers a specific SQL
concept or query type. The script connects to the local `chinook.db`
database, executes the example queries where appropriate, and writes
the results into corresponding lesson files under the `lessons`
directory. Lessons that modify data are illustrated but not executed
against the database to avoid side effects.

Run this script from the root of the project directory:

    python generate_lessons.py

It will populate the `lessons` directory with numbered Markdown
documents. Each document contains a title, a brief explanation of the
concept, the SQL query, and a sample result where applicable.
"""

import os
import sqlite3
from textwrap import dedent
from typing import List, Dict

import pandas as pd


def df_to_markdown(df: pd.DataFrame) -> str:
    """Convert a pandas DataFrame to a simple Markdown table without relying
    on external dependencies. Each column becomes a header and rows are
    separated by vertical bars. Indices are omitted.

    Args:
        df: The DataFrame to convert.

    Returns:
        A string containing the Markdown table.
    """
    # Build header row
    header_cells = [str(col) for col in df.columns]
    header = '| ' + ' | '.join(header_cells) + ' |'
    # Build separator row (align left)
    separator = '| ' + ' | '.join(['---' for _ in df.columns]) + ' |'
    # Build data rows
    rows = []
    for _, row in df.iterrows():
        cells = [str(cell) for cell in row]
        rows.append('| ' + ' | '.join(cells) + ' |')
    return '\n'.join([header, separator] + rows)


def fetch_sample_results(conn: sqlite3.Connection, query: str, limit: int = 5) -> str:
    """Execute a query and return a Markdown-formatted table of the first
    few rows of the result set. If the query fails (e.g. for DDL
    statements), an empty string is returned.

    Args:
        conn: SQLite connection object.
        query: SQL query to execute.
        limit: Maximum number of rows to include in the output.

    Returns:
        A string containing a Markdown table representation of the
        query result, or an empty string if no sample should be
        provided.
    """
    try:
        # Strip trailing semicolons to avoid errors when executing via pandas.
        clean_query = query.strip().rstrip(';')
        # Use pandas to run the query and fetch a small number of rows.
        df = pd.read_sql_query(clean_query, conn)
        if df.empty:
            return "_No rows returned._"
        if len(df) > limit:
            df = df.head(limit)
        # Convert DataFrame to a Markdown table without external dependencies.
        return df_to_markdown(df)
    except Exception:
        # For queries that cannot be executed (e.g. inserts/updates) we skip.
        return ""


def generate_lessons(db_path: str, lessons: List[Dict[str, str]], lesson_dir: str) -> None:
    """Generate lesson markdown files based on provided lesson
    definitions.

    Args:
        db_path: Path to the SQLite database.
        lessons: List of lesson definitions. Each definition is a
            dictionary with keys `slug`, `title`, `description`,
            `query`, and `run` indicating whether to execute the query.
        lesson_dir: Directory where lesson files should be saved.
    """
    os.makedirs(lesson_dir, exist_ok=True)
    conn = sqlite3.connect(db_path)
    for lesson in lessons:
        filename = f"{lesson['slug']}.md"
        path = os.path.join(lesson_dir, filename)
        # Prepare content
        content = [f"# {lesson['title']}\n"]
        # Wrap the description to 80 characters per line
        description = dedent(lesson['description']).strip()
        content.append(description + "\n")
        # Include the SQL query as a fenced code block
        content.append("```sql")
        content.append(lesson['query'].strip())
        content.append("```")
        # If the lesson's query should be executed, fetch sample results
        if lesson.get("run", True):
            result_md = fetch_sample_results(conn, lesson['query'])
            if result_md:
                content.append("**Sample result (first few rows):**")
                content.append(result_md)
        # Write the file
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(content))
    conn.close()


def main():
    # Define the list of lessons. Each lesson covers a single SQL concept.
    # The `run` flag indicates whether the query should be executed to
    # capture sample results. Data manipulation or DDL statements are
    # typically not run to avoid altering the database.
    lessons = [
        {
            "slug": "01_select_basic",
            "title": "Basic SELECT – retrieve all columns",
            "description": """
            The `SELECT` statement is the foundation of querying in SQL. A
            basic `SELECT` retrieves all columns and rows from a table. In the
            Chinook database, the `artists` table stores information about
            musical artists. This query returns the first five artists and
            shows every column in the table.
            """,
            "query": "SELECT * FROM artists LIMIT 5;",
            "run": True,
        },
        {
            "slug": "02_select_columns",
            "title": "Selecting specific columns",
            "description": """
            Instead of selecting every column, you can specify exactly which
            columns you want to see. Here we select the `FirstName` and
            `LastName` columns from the `employees` table to list the staff
            names without showing their contact details or other fields.
            """,
            "query": "SELECT FirstName, LastName FROM employees;",
            "run": True,
        },
        {
            "slug": "03_where_clause",
            "title": "Filtering rows with WHERE",
            "description": """
            The `WHERE` clause filters rows based on a condition. In this
            example we retrieve all customers from the United States. Only
            rows where the `Country` column is `USA` are returned.
            """,
            "query": "SELECT * FROM customers WHERE Country = 'USA';",
            "run": True,
        },
        {
            "slug": "04_where_and",
            "title": "Combining conditions with AND",
            "description": """
            You can combine multiple conditions using the `AND` operator. This
            query finds customers in the USA who are also located in
            California. Both conditions must be true for a row to be included.
            """,
            "query": "SELECT * FROM customers WHERE Country = 'USA' AND State = 'CA';",
            "run": True,
        },
        {
            "slug": "05_where_or",
            "title": "Combining conditions with OR",
            "description": """
            The `OR` operator allows rows that meet at least one of the
            specified conditions. This query returns customers who are in
            either Brazil or France.
            """,
            "query": "SELECT * FROM customers WHERE Country = 'Brazil' OR Country = 'France';",
            "run": True,
        },
        {
            "slug": "06_where_in",
            "title": "Testing membership with IN",
            "description": """
            The `IN` operator checks whether a value matches any value in a
            list. This query selects all genres whose name is either 'Rock' or
            'Jazz'.
            """,
            "query": "SELECT * FROM genres WHERE Name IN ('Rock', 'Jazz');",
            "run": True,
        },
        {
            "slug": "07_where_between",
            "title": "Filtering by range with BETWEEN",
            "description": """
            Use `BETWEEN` to filter numeric values within a specified range.
            Here we select tracks priced between $0.99 and $1.99 inclusive. The
            `UnitPrice` column stores the price of each track.
            """,
            "query": "SELECT Name, UnitPrice FROM tracks WHERE UnitPrice BETWEEN 0.99 AND 1.99;",
            "run": True,
        },
        {
            "slug": "08_order_by",
            "title": "Sorting results with ORDER BY",
            "description": """
            The `ORDER BY` clause sorts the result set. By default it sorts in
            ascending order. This example lists employees by last name
            alphabetically.
            """,
            "query": "SELECT FirstName, LastName FROM employees ORDER BY LastName;",
            "run": True,
        },
        {
            "slug": "09_order_by_desc",
            "title": "Descending order sorting",
            "description": """
            Add the `DESC` keyword after a column name to sort in descending
            order. Here we list the five most expensive tracks first by
            ordering on `UnitPrice` descending.
            """,
            "query": "SELECT Name, UnitPrice FROM tracks ORDER BY UnitPrice DESC LIMIT 5;",
            "run": True,
        },
        {
            "slug": "10_group_by",
            "title": "Grouping data with GROUP BY",
            "description": """
            The `GROUP BY` clause aggregates rows sharing the same value of
            specified columns. This query counts how many customers are in
            each country.
            """,
            "query": "SELECT Country, COUNT(*) AS CustomerCount FROM customers GROUP BY Country ORDER BY CustomerCount DESC;",
            "run": True,
        },
        {
            "slug": "11_having",
            "title": "Filtering groups with HAVING",
            "description": """
            After grouping rows, use the `HAVING` clause to filter the
            aggregated results. This query shows countries with more than five
            customers.
            """,
            "query": "SELECT Country, COUNT(*) AS CustomerCount FROM customers GROUP BY Country HAVING COUNT(*) > 5 ORDER BY CustomerCount DESC;",
            "run": True,
        },
        {
            "slug": "12_count",
            "title": "Counting rows with COUNT",
            "description": """
            `COUNT(*)` returns the total number of rows in a table. Here we
            count the number of tracks in the database.
            """,
            "query": "SELECT COUNT(*) AS TrackCount FROM tracks;",
            "run": True,
        },
        {
            "slug": "13_sum",
            "title": "Summing values with SUM",
            "description": """
            The `SUM` function adds up all values of a numeric column. This
            query calculates the total of all invoice amounts.
            """,
            "query": "SELECT SUM(Total) AS TotalRevenue FROM invoices;",
            "run": True,
        },
        {
            "slug": "14_avg",
            "title": "Calculating averages with AVG",
            "description": """
            Use the `AVG` function to compute the mean value of a numeric
            column. Here we determine the average track price.
            """,
            "query": "SELECT AVG(UnitPrice) AS AveragePrice FROM tracks;",
            "run": True,
        },
        {
            "slug": "15_min_max",
            "title": "Finding minimum and maximum values",
            "description": """
            The `MIN` and `MAX` functions return the smallest and largest
            values in a column. This example shows the cheapest and most
            expensive track prices.
            """,
            "query": "SELECT MIN(UnitPrice) AS MinPrice, MAX(UnitPrice) AS MaxPrice FROM tracks;",
            "run": True,
        },
        {
            "slug": "16_distinct",
            "title": "Removing duplicates with DISTINCT",
            "description": """
            The `DISTINCT` keyword removes duplicate values from the result set.
            This query lists all unique countries where customers reside.
            """,
            "query": "SELECT DISTINCT Country FROM customers ORDER BY Country;",
            "run": True,
        },
        {
            "slug": "17_inner_join",
            "title": "Combining tables with INNER JOIN",
            "description": """
            Joins combine rows from two or more tables based on related columns.
            An `INNER JOIN` returns only rows that have matching values on
            both sides. Here we join `albums` with `artists` to show each
            album's title alongside the artist's name.
            """,
            "query": "SELECT albums.Title AS Album, artists.Name AS Artist FROM albums JOIN artists ON albums.ArtistId = artists.ArtistId ORDER BY Artist, Album LIMIT 10;",
            "run": True,
        },
        {
            "slug": "18_left_join",
            "title": "Including unmatched rows with LEFT JOIN",
            "description": """
            A `LEFT JOIN` (or left outer join) returns all rows from the left
            table and the matching rows from the right table. If there is no
            match, the result contains NULLs for the right table's columns.
            This query lists customers and their invoices, if any. Customers
            without invoices still appear in the result.
            """,
            "query": "SELECT customers.FirstName || ' ' || customers.LastName AS Customer, invoices.InvoiceId, invoices.Total FROM customers LEFT JOIN invoices ON customers.CustomerId = invoices.CustomerId ORDER BY Customer LIMIT 10;",
            "run": True,
        },
        {
            "slug": "19_right_join",
            "title": "Simulating a RIGHT JOIN in SQLite",
            "description": """
            SQLite does not support the `RIGHT JOIN` syntax, but you can achieve
            the same effect by swapping the tables and using a `LEFT JOIN`.
            This query finds invoices and their customers, including invoices
            that might not have a matching customer (although in this
            database every invoice has a valid customer). The principle is
            explained rather than demonstrated with missing data.
            """,
            "query": "SELECT invoices.InvoiceId, customers.FirstName || ' ' || customers.LastName AS Customer, invoices.Total FROM invoices LEFT JOIN customers ON customers.CustomerId = invoices.CustomerId LIMIT 10;",
            "run": True,
        },
        {
            "slug": "20_cross_join",
            "title": "Creating a Cartesian product with CROSS JOIN",
            "description": """
            A `CROSS JOIN` returns the Cartesian product of two tables, meaning
            each row of the first table is paired with each row of the second.
            This can quickly produce large result sets. Here we cross join
            employees and media types and show only a few rows to illustrate
            the pattern.
            """,
            "query": "SELECT employees.FirstName || ' ' || employees.LastName AS Employee, media_types.Name AS MediaType FROM employees CROSS JOIN media_types LIMIT 10;",
            "run": True,
        },
        {
            "slug": "21_self_join",
            "title": "Referencing a table to itself with SELF JOIN",
            "description": """
            A self join is a join of a table with itself. It's useful for
            hierarchical relationships stored in a single table. In the
            employees table, the `ReportsTo` column refers to the manager of
            each employee. This query pairs employees with their managers.
            """,
            "query": "SELECT e.FirstName || ' ' || e.LastName AS Employee, m.FirstName || ' ' || m.LastName AS Manager FROM employees e LEFT JOIN employees m ON e.ReportsTo = m.EmployeeId ORDER BY Employee LIMIT 10;",
            "run": True,
        },
        {
            "slug": "22_union",
            "title": "Combining result sets with UNION",
            "description": """
            The `UNION` operator combines the results of two queries and
            eliminates duplicate rows. Here we list all unique countries that
            appear in either the customers or employees tables. Each country
            appears only once in the final set.
            """,
            "query": "SELECT Country FROM customers UNION SELECT Country FROM employees ORDER BY Country;",
            "run": True,
        },
        {
            "slug": "23_union_all",
            "title": "Including duplicates with UNION ALL",
            "description": """
            `UNION ALL` also combines results from two queries but keeps
            duplicates. This query returns the list of countries from the
            customers table twice, so countries with more customers will appear
            multiple times.
            """,
            "query": "SELECT Country FROM customers UNION ALL SELECT Country FROM customers ORDER BY Country LIMIT 20;",
            "run": True,
        },
        {
            "slug": "24_except",
            "title": "Finding differences with EXCEPT",
            "description": """
            The `EXCEPT` operator returns rows from the first query that are
            not present in the second. This example lists countries that have
            customers but no employees. Note that the country names are
            compared across the two tables.
            """,
            "query": "SELECT Country FROM customers EXCEPT SELECT Country FROM employees ORDER BY Country;",
            "run": True,
        },
        {
            "slug": "25_intersect",
            "title": "Finding common values with INTERSECT",
            "description": """
            The `INTERSECT` operator returns rows that are common to both
            queries. This query finds countries that appear in both the
            customers and employees tables.
            """,
            "query": "SELECT Country FROM customers INTERSECT SELECT Country FROM employees ORDER BY Country;",
            "run": True,
        },
        {
            "slug": "26_subquery",
            "title": "Using subqueries for comparisons",
            "description": """
            A subquery is a query nested within another query. In this
            example we select tracks whose price is above the average track
            price. The subquery computes the average price across all tracks.
            """,
            "query": "SELECT Name, UnitPrice FROM tracks WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM tracks) ORDER BY UnitPrice DESC LIMIT 10;",
            "run": True,
        },
        {
            "slug": "27_exists",
            "title": "Checking for existence with EXISTS",
            "description": """
            The `EXISTS` operator tests whether a subquery returns any rows. In
            this query we list artists who have at least one album in the
            database. The subquery checks for the existence of albums linked
            to each artist.
            """,
            "query": "SELECT Name FROM artists a WHERE EXISTS (SELECT 1 FROM albums al WHERE al.ArtistId = a.ArtistId) ORDER BY Name LIMIT 10;",
            "run": True,
        },
        {
            "slug": "28_case",
            "title": "Adding conditional logic with CASE",
            "description": """
            The `CASE` expression returns a value based on conditional
            logic. This query labels tracks as 'Expensive' if the price is
            greater than $1.00 and 'Cheap' otherwise. Labels can be used in
            result sets just like any other computed column.
            """,
            "query": "SELECT Name, UnitPrice, CASE WHEN UnitPrice > 1.00 THEN 'Expensive' ELSE 'Cheap' END AS PriceCategory FROM tracks ORDER BY UnitPrice DESC LIMIT 10;",
            "run": True,
        },
        {
            "slug": "29_insert",
            "title": "Inserting rows into a table",
            "description": """
            `INSERT` adds new rows to a table. In practice you would insert
            data into existing business tables, but here we create a simple
            temporary table to demonstrate. Create the table, insert a row,
            and query the contents to see the result. (These statements are
            not executed automatically by this tutorial.)
            """,
            "query": """
            -- Create a temporary table for demonstration
            CREATE TABLE IF NOT EXISTS demo_insert (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT
            );

            -- Insert a new row
            INSERT INTO demo_insert (Name) VALUES ('Example Row');

            -- Query the table to see the inserted row
            SELECT * FROM demo_insert;
            """,
            "run": False,
        },
        {
            "slug": "30_update",
            "title": "Updating existing rows",
            "description": """
            The `UPDATE` statement modifies existing rows. Using the same
            temporary table from the previous lesson, change the row's name
            and then retrieve it to verify the update. (These statements
            are illustrative and not executed automatically.)
            """,
            "query": """
            -- Update the row in the demo_insert table
            UPDATE demo_insert SET Name = 'Updated Row' WHERE Id = 1;

            -- Query the table to see the updated data
            SELECT * FROM demo_insert;
            """,
            "run": False,
        },
        {
            "slug": "31_delete",
            "title": "Deleting rows",
            "description": """
            Use `DELETE` to remove rows from a table. Continuing with the
            `demo_insert` table, delete the row we previously inserted and
            then select from the table to confirm it's empty. (These
            statements are illustrative and not executed automatically.)
            """,
            "query": """
            -- Delete the row from the demo_insert table
            DELETE FROM demo_insert WHERE Id = 1;

            -- Query the table to confirm deletion
            SELECT * FROM demo_insert;
            """,
            "run": False,
        },
        {
            "slug": "32_create_table",
            "title": "Creating new tables",
            "description": """
            The `CREATE TABLE` statement defines a new table. Here we create
            a simple table called `example_table` with an integer primary key
            and a text column. You would normally run this once during
            database setup. (This statement is not executed automatically.)
            """,
            "query": """
            CREATE TABLE example_table (
                Id INTEGER PRIMARY KEY,
                Description TEXT
            );
            """,
            "run": False,
        },
        {
            "slug": "33_alter_table",
            "title": "Changing a table with ALTER TABLE",
            "description": """
            Use `ALTER TABLE` to modify an existing table structure. In this
            example we add a `CreatedAt` column to the `example_table` to
            record when each row was created. (This statement is not
            executed automatically.)
            """,
            "query": "ALTER TABLE example_table ADD COLUMN CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP;",
            "run": False,
        },
        {
            "slug": "34_drop_table",
            "title": "Removing tables with DROP TABLE",
            "description": """
            When a table is no longer needed, `DROP TABLE` permanently
            removes it and its data. Here we drop the `example_table` we
            created in previous lessons. (This statement is not executed
            automatically.)
            """,
            "query": "DROP TABLE IF EXISTS example_table;",
            "run": False,
        },
        {
            "slug": "35_create_view",
            "title": "Creating reusable queries with VIEWs",
            "description": """
            A view is a saved query that can be treated like a table. This
            example creates a view combining customer names and their invoice
            totals. You can query the view just like a normal table. (The
            creation statement is not executed automatically, but the
            subsequent SELECT demonstrates how you would use it.)
            """,
            "query": """
            -- Create the view
            CREATE VIEW IF NOT EXISTS customer_invoices AS
            SELECT c.FirstName || ' ' || c.LastName AS Customer,
                   i.Total
              FROM customers c
              JOIN invoices i ON c.CustomerId = i.CustomerId;

            -- Query the view
            SELECT * FROM customer_invoices ORDER BY Total DESC LIMIT 10;
            """,
            "run": False,
        },
        {
            "slug": "36_create_index",
            "title": "Improving performance with indexes",
            "description": """
            An index speeds up lookups on a table column. Creating too many
            indexes can slow down writes, so it’s important to index only
            where needed. This example creates an index on the `AlbumId`
            column of the `tracks` table to improve joins and lookups by
            album. (This statement is not executed automatically.)
            """,
            "query": "CREATE INDEX idx_tracks_albumid ON tracks (AlbumId);",
            "run": False,
        },
        {
            "slug": "37_transactions",
            "title": "Ensuring atomicity with transactions",
            "description": """
            A transaction groups multiple statements into a single unit of
            work. If any statement fails, the entire transaction can be
            rolled back. This example shows how to begin a transaction,
            update a record, and then roll back the change. (These
            statements are illustrative and not executed automatically.)
            """,
            "query": """
            -- Start a transaction
            BEGIN TRANSACTION;

            -- Example update: increase the price of a specific track
            UPDATE tracks SET UnitPrice = UnitPrice + 0.10 WHERE TrackId = 1;

            -- Roll back the change
            ROLLBACK;
            """,
            "run": False,
        },
        {
            "slug": "38_window_functions",
            "title": "Using window functions",
            "description": """
            Window functions perform calculations across sets of rows that
            relate to the current row. The `ROW_NUMBER()` function assigns
            a unique sequential integer to rows ordered by price. This query
            ranks tracks by descending price.
            """,
            "query": "SELECT TrackId, Name, UnitPrice, ROW_NUMBER() OVER (ORDER BY UnitPrice DESC) AS PriceRank FROM tracks ORDER BY UnitPrice DESC LIMIT 10;",
            "run": True,
        },
        {
            "slug": "39_cte",
            "title": "Simplifying queries with common table expressions (CTE)",
            "description": """
            A CTE is a named temporary result set defined within a query.
            This example uses a simple CTE to select the top five invoices by
            total amount. The CTE improves readability by separating the
            logic for selecting the top invoices from the outer query.
            """,
            "query": "WITH TopInvoices AS (SELECT InvoiceId, Total FROM invoices ORDER BY Total DESC LIMIT 5) SELECT * FROM TopInvoices ORDER BY Total DESC;",
            "run": True,
        },
        {
            "slug": "40_recursive_cte",
            "title": "Working with hierarchical data using recursive CTEs",
            "description": """
            Recursive CTEs allow you to query hierarchical relationships,
            such as an organizational chart. In the Chinook employees table,
            the `ReportsTo` column references a manager. This query builds
            a hierarchy starting from the top-level manager and recursively
            traverses subordinate employees. The result shows each
            employee alongside their manager chain. Not all SQLite
            environments support recursive CTEs; if not supported, this
            example may not execute. Results are limited for readability.
            """,
            "query": """
            WITH RECURSIVE employee_hierarchy AS (
                -- Anchor member: select top-level employees (no manager)
                SELECT EmployeeId, FirstName || ' ' || LastName AS Name,
                       ReportsTo, 0 AS Level,
                       CAST(FirstName || ' ' || LastName AS TEXT) AS Path
                  FROM employees
                 WHERE ReportsTo IS NULL

                UNION ALL

                -- Recursive member: select employees reporting to the
                -- previous level
                SELECT e.EmployeeId, e.FirstName || ' ' || e.LastName AS Name,
                       e.ReportsTo, h.Level + 1 AS Level,
                       CAST(h.Path || ' -> ' || e.FirstName || ' ' || e.LastName AS TEXT) AS Path
                  FROM employees e
                  JOIN employee_hierarchy h ON e.ReportsTo = h.EmployeeId
            )
            SELECT EmployeeId, Name, Level, Path FROM employee_hierarchy ORDER BY Level, Name LIMIT 20;
            """,
            "run": True,
        },
    ]

    db_path = os.path.join('sql_tutorial_project', 'chinook.db')
    lesson_dir = os.path.join('sql_tutorial_project', 'lessons')
    generate_lessons(db_path, lessons, lesson_dir)


if __name__ == '__main__':
    main()