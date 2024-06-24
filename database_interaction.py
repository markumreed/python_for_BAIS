#database_interaction.py
import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn, create_table_sql):
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()

def insert_data(conn, table, data):
    placeholders = ", ".join("?" * len(data))
    sql = f"INSERT INTO {table} VALUES ({placeholders})"
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()

def query_data(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()