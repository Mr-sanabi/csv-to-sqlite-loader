import csv

def read_csv(csv_file):
    try:
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            headers = reader.fieldnames
            rows = list(reader)

            return headers, rows
    except FileNotFoundError:
        print(f"File not found: {csv_file}")
        return [], []