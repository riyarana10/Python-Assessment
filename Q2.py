# Create a python script which reads from a csv file and inserts multiple employees data in the database at once.

import csv
import mysql.connector

conn = mysql.connector.connect(host='localhost', password='Password1!', user='root', database='test')

if conn.is_connected():
    print("Connection established")

def insert_employees_from_csv(csv_file):
    # Connect to the database
    cursor = conn.cursor()

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if not row:
                print("Skipping empty row.")
                continue

            if len(row) != 8:
                print(f"Skipping row with insufficient data: {row}")
                continue

            emp_id, emp_name, email, phone, PF_id, date_of_joining, dob, department = row

            sqlQuery = "INSERT INTO employees (emp_id, emp_name, email, phone, PF_id, date_of_joining, dob, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (emp_id, emp_name, email, phone, PF_id, date_of_joining, dob, department)

            try:
                cursor.execute(sqlQuery, values)
            except mysql.connector.Error as err:
                print(f"Error while inserting data for employee ID {emp_id}: {err}")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Example usage
csv_file = 'employees.csv'
insert_employees_from_csv(csv_file)
