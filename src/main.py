import argparse
import sys
from loader import read_csv
from db import connect_db, create_table, insert_rows, count_rows, preview_rows


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
    headers, rows = read_csv(args.csv_file)

    if not headers or not rows:
        print(f"Error: failed to read CSV file '{args.csv_file}' or the file is empty.")
        sys.exit(1)

    connection = connect_db(args.db_file)

    create_table(connection, args.table_name, headers)
    insert_rows(connection, args.table_name, headers, rows)
    count = count_rows(connection, args.table_name)

    summary = (
        f"Table created: {args.table_name}\n"
        f"Rows imported: {len(rows)}\n"
        f"Rows in table: {count}\n"
        f"Database file: {args.db_file}\n"
        )
    

    if args.preview:
        previews = preview_rows(connection, args.table_name, args.limit)
        summary = summary + "Preview rows:\n"
        for preview in previews:
            summary = summary + str(preview) +  "\n"

    connection.close()

    print(summary)

if __name__ == "__main__":
    main()