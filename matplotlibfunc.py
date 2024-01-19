import mysql.connector
#import csv
import pandas as pd
from mysql.connector import Error
import matplotlib.pyplot as plt

#PLOTTING Function - matplotlib
def compare_passengers(conn, table_name):
    """Compare domestic and international passengers using a bar chart."""
    try:
        cursor = conn.cursor()

        # Query to get the sum of passengers for domestic and international flights
        query_domestic = f"SELECT SUM(Passengers_Domestic) FROM {table_name}"
        cursor.execute(query_domestic)
        result_domestic = cursor.fetchone()

        query_international = f"SELECT SUM(Passengers_International) FROM {table_name}"
        cursor.execute(query_international)
        result_international = cursor.fetchone()

        # Prepare data for plotting
        labels = ['Domestic', 'International']
        values = [result_domestic[0], result_international[0]]

        # Plotting the bar chart
        plt.bar(labels, values, color=['blue', 'green'])
        plt.title('Comparison of Passengers' )
        plt.xlabel('Flight Location')
        plt.ylabel('Total Passengers')
        plt.show()

    except Error as e:
        print(e)