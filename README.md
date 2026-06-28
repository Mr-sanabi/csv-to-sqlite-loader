# CSV to SQLite Loader

A small Python CLI tool that imports CSV data into a SQLite database table.

The tool reads CSV headers, creates a SQLite table from them, imports all rows, and verifies the result with a simple row count query.

## Features

* Load CSV files into a SQLite `.db` database
* Automatically create a table based on CSV headers
* Import rows using Python's built-in `sqlite3` module
* Replace-mode import: the target table is recreated on each run
* Simple CLI interface with `argparse`
* Row count check after import
* No external dependencies

## Tech Stack

* Python
* SQLite
* `sqlite3`
* `csv`
* `argparse`

## Project Structure

```text
csv-to-sqlite-loader/
  src/
    main.py
    loader.py
    db.py
    logger_config.py

  data/
    .gitkeep

  README.md
  requirements.txt
  .gitignore
```

## Usage

```bash
python src/main.py data/products.csv data/products.db products
```

Arguments:

```text
data/products.csv   Path to the input CSV file
data/products.db    Path to the SQLite database file
products            Target table name
```

## Example CSV

```csv
product_title,product_url,description,price,compare_at_price,variant_title,sku,image_url
Men's Dasher NZ,https://example.com/product,Running shoes,140.00,,8,A12647M080,https://example.com/image.jpg
Men's Dasher NZ,https://example.com/product,Running shoes,120.00,,8.5,A12647M085,https://example.com/image.jpg
Men's Dasher NZ,https://example.com/product,Running shoes,150.00,,9,A12647M090,https://example.com/image.jpg
```

## Example Output

```text
Table created: products
Rows imported: 5
Rows in table: 5
Database file: data/products.db
```

## How It Works

1. The CLI receives a CSV file path, database file path, and table name.
2. The CSV file is read with `csv.DictReader`.
3. CSV headers are used to create table columns.
4. The target table is dropped if it already exists.
5. A new SQLite table is created.
6. CSV rows are inserted into the table.
7. A `SELECT COUNT(*)` query checks how many rows are stored.

## Import Mode

This project uses replace-mode import.

Each run recreates the target table before importing the CSV data. This prevents duplicate rows when the same command is executed multiple times.

## Notes

All columns are created as `TEXT` for simplicity and reliability.

CSV files are read as strings by default, so this MVP keeps the import process simple. Type conversion such as `REAL` for prices or `INTEGER` for quantities can be added later.

## What I Practiced

* Reading CSV files with `csv.DictReader`
* Working with SQLite from Python
* Creating SQL tables dynamically from CSV headers
* Inserting rows into a database
* Running basic SQL queries from Python
* Building a small CLI data tool
