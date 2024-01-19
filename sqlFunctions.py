import mysql.connector
#import csv
import pandas as pd
from mysql.connector import Error
import matplotlib.pyplot as plt



# SQL Functions
def create_connection1():
    """Create a database connection."""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='dataset_test',
            user='root',
            password='8913'
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(e)

def create_table1(conn, table_name, columns1):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns1})"
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully.")
    except Error as e:
        print(e)

def create_table2(conn, table_name, columns2):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns2})"
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully.")
    except Error as e:
        print(e)

def create_table3(conn, table_name, columns3):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns3})"
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully.")
    except Error as e:
        print(e)

def create_table4(conn, table_name, columns4):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns4})"
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully.")
    except Error as e:
        print(e)

def insert_data(conn, table_name, data):
    """Insert data into the table."""
    try:
        cursor = conn.cursor()
        for index, row in data.iterrows():
            # Replace NaN values with None (NULL in MySQL)
            row = row.where(pd.notna(row), None)

            # Use placeholders in the query to handle NULL values
            insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))})"
            cursor.execute(insert_query, tuple(row))
        conn.commit()
        print("Data inserted successfully.")
    except Error as e:
        print(e)

def total_domestic_passengers_from_db(conn, table_name):
    """Retrieve the total domestic passengers from the database."""
    try:
        cursor = conn.cursor()
        query = f"SELECT SUM(Passengers_Domestic) FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        total_passengers = result[0]
        print(f"Total domestic passengers: {total_passengers}")
    except Error as e:
        print(e)

def total_international_passengers_from_db(conn, table_name):
    """Retrieve the total domestic passengers from the database."""
    try:
        cursor = conn.cursor()
        query = f"SELECT SUM(Passengers_International) FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        total_passengers = result[0]
        print(f"Total international passengers: {total_passengers}")
    except Error as e:
        print(e)

def highest_asm_domestic_from_db(conn, table_name):
    """Retrieve the highest ASM (Airline Seat Mile) for domestic flights from the database."""
    try:
        cursor = conn.cursor()
        query = f"SELECT MAX(ASM_Domestic) FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        highest_asm_domestic = result[0]
        print(f"Highest ASM for Domestic flights: {highest_asm_domestic}")
    except Error as e:
        print(e)

def highest_asm_international_from_db(conn, table_name):
    """Retrieve the highest ASM (Airline Seat Mile) for international flights from the database."""
    try:
        cursor = conn.cursor()
        query = f"SELECT MAX(ASM_International) FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        highest_asm_international = result[0]
        print(f"Highest ASM for International flights: {highest_asm_international}")
    except Error as e:
        print(e)

def highest_rpm_domestic_from_db(conn, table_name):
    """Retrieve the highest ASM (Airline Seat Mile) for domestic flights from the database."""
    try:
        cursor = conn.cursor()
        query = f"SELECT MAX(RPM_Domestic) FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        highest_rpm_domestic = result[0]
        print(f"Highest RPM for Domestic flights: {highest_rpm_domestic}")
    except Error as e:
        print(e)

def highest_rpm_international_from_db(conn, table_name):
    """Retrieve the highest ASM (Airline Seat Mile) for international flights from the database."""
    try:
        cursor = conn.cursor()
        query = f"SELECT MAX(RPM_International) FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        highest_rpm_international = result[0]
        print(f"Highest ASM for International flights: {highest_rpm_international}")
    except Error as e:
        print(e)