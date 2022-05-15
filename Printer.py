import csv
import os
from datetime import datetime


def writeToCSV(schema):
    date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    if not os.path.isfile('Stock_values.csv'):
        with open('stock_values.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            headers = [company["name"] for company in schema]
            headers.append('Date/Time')
            writer.writerow(headers)
    with open('Stock_values.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        values = [company["value"] for company in schema]
        values.append(date)
        writer.writerow(values)