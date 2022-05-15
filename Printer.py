import csv
import os


def write_val(values):
    if not os.path.isfile('Stock_values.csv'):
        with open('Stock_values.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Dutch Shell", "AJ Bell", "Gamestop", "United Utilities", "Date/Time"])
    with open('Stock_values.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(x for x in values)