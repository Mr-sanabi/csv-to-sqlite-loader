# CSV to SQLite Loader

A Python CLI that imports a CSV into SQLite and reports the stored row count. Uses only the standard library.

## Run

**Each run drops and recreates the target table. Back up existing data first.**

```bash
python src/main.py data/products.csv data/products.db products
```

Arguments: input CSV, database file, and target table name.
CSV headers become column names; all columns are stored as `TEXT`, with no automatic numeric conversion. Add `--preview --limit 5` to preview imported rows.
