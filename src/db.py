import sqlite3

def connect_db(db_file):
    connection = sqlite3.connect(db_file)
    return connection

def create_table(connection, table_name, headers):
    columns  = []

    for header in headers:
        column = f"{header} TEXT"
        columns.append(column)

    columns_sql = ", ".join(columns)

    drop_table_sql = f"DROP TABLE IF EXISTS {table_name}"

    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})"

    cursor = connection.cursor()
    cursor.execute(drop_table_sql)
    cursor.execute(query)
    connection.commit()

def insert_rows(connection, table_name, headers, rows):
    
    columns_sql = ", ".join(headers)
    placeholders = ", ".join(["?"] * len(headers))
    
    sql =  F"INSERT INTO {table_name} ({columns_sql}) VALUES ({placeholders})"

    cursor = connection.cursor()

    for row in rows:
        values = []
        for header in headers:
            values.append(row[header])
        
        cursor.execute(sql, values)
        
    
    connection.commit()


def count_rows(connection, table_name):
    cursor = connection.cursor()

    sql = f"SELECT COUNT(*) FROM {table_name}"
    
    cursor.execute(sql)

    result = cursor.fetchone()

    return result[0]

def preview_rows(connection, table_name, limit):
    cursor = connection.cursor()

    sql = f"SELECT * FROM {table_name} LIMIT {limit}"
    
    cursor.execute(sql)

    result = cursor.fetchall()

    return result

