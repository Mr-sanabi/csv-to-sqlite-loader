import argparse
import sys
from loader import read_csv
from db import connect_db, create_table, insert_rows, count_rows


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file")
    parser.add_argument("db_file")
    parser.add_argument("table_name")
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

    connection.close()

    summary = (
        f"Table created: {args.table_name}\n"
        f"Rows imported: {len(rows)}\n"
        f"Rows in table: {count}\n"
        f"Database file: {args.db_file}")
    
    print(summary)

if __name__ == "__main__":
    main()