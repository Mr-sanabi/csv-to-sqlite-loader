import argparse
import sys
import logging
from loader import read_csv
from db import connect_db, create_table, insert_rows, count_rows, preview_rows
from logger_config import setup_logging


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file")
    parser.add_argument("db_file")
    parser.add_argument("table_name")
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--limit", type=int, default=5)
    return parser.parse_args()


def main():
    args = parse_args()
    setup_logging()
    logging.info("Starting program")
    headers, rows = read_csv(args.csv_file)

    if not headers or not rows:
        logging.info(f"Failed to read CSV file '{args.csv_file}' or the file is empty.")
        sys.exit(1)

    logging.info("CSV file read successfully")

    connection = connect_db(args.db_file)
    logging.info("Database connection established")

    create_table(connection, args.table_name, headers)
    logging.info("Table created")
    insert_rows(connection, args.table_name, headers, rows)
    logging.info("Rows imported into table")
    count = count_rows(connection, args.table_name)
    logging.info("Row count calculated")

    summary = (
        f"==================== SUMMARY ====================\n"
        f"Table: {args.table_name}\n"
        f"Imported rows: {len(rows)}\n"
        f"Rows in table: {count}\n"
        f"Database: {args.db_file}\n"
        f"================================================="
    )

    if args.preview:
        previews = preview_rows(connection, args.table_name, args.limit)
        logging.info("Preview rows requested")
        summary += "\nPreview rows:\n"
        for preview in previews:
            summary += str(preview) + "\n"

    connection.close()
    logging.info("Database connection closed")

    print(summary)


if __name__ == "__main__":
    main()