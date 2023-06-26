import mysql.connector
import csv
# from email_validator import validate_email, EmailNotValidError
import re

conn = mysql.connector.connect(host='localhost', password='Password1!',user='root', database='test')
if conn.is_connected():
    print("connection established")
    

# testing connection establishment
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM teacher")
# # result = cursor.fetchone()
# result = cursor.fetchall()
# print("Example data from the database:")
# print(result)
# # Close the connection
# conn.close()



class Employee:
    
     def __init__(self, emp_id, emp_name, email,  phone, PF_id, date_of_joining, dob, department):
        self.emp_id = emp_id
        # self.email = email
        self.emp_name = emp_name
        self.email = email
        self.phone = phone
        self.PF_id = PF_id
        self.date_of_joining = date_of_joining
        self.dob = dob
        self.department = department
    
     def add_employee(self):
        if not Employee.is_employee_id_unique(self.emp_id):
            print("Employee ID already exists. Please try again.")
            return
        
        if not Employee.checkEmail(self.email):
            print("Invalid email format. Please try again.")
            return
        
        if not Employee.is_valid_phone_number(self.phone):
            print("Invalid phone number format. Please try again.")
            return

        cursor = conn.cursor()
        query = "INSERT INTO employees (emp_id, emp_name, email, phone, PF_id, date_of_joining, dob, department) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (self.emp_id, self.emp_name, self.email, self.phone, self.PF_id, self.date_of_joining,
                  self.dob, self.department)
        cursor.execute(query, values)
        conn.commit()
        print("Employee added successfully.")
    
    
     def update_employee_phone(emp_id):
        query = '''
        SELECT * FROM employees WHERE emp_id = %s
        '''
        cursor = conn.cursor()
        cursor.execute(query, (emp_id,))
        employee = cursor.fetchone()

        if employee:
            phone = input("Enter the new phone number: ")
            if Employee.is_valid_phone_number(phone):
                query = '''
                UPDATE employees
                SET phone = %s
                WHERE emp_id = %s
                '''
                values = (phone, emp_id)
                cursor.execute(query, values)
                conn.commit()
                print("Phone number updated successfully!")
            else:
                print("Invalid phone number!")
        else:
            print("Employee not found!")
         
         
    
     def is_employee_id_unique(emp_id):
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM employees WHERE emp_id = %s"
        cursor.execute(query, (emp_id,))
        count = cursor.fetchone()[0]
        return count == 0
        
        
     
     def checkEmail(email):
        email = str(email)
        regex = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
        if re.fullmatch(regex, email):
            return True
        else:
            return False
    
    
     def is_valid_phone_number(phone):
         if len(phone) < 10 or not phone.isdigit():
             return False
         return True
     
     
     def employees_joined_in_2021_to_csv():
        cursor = conn.cursor()
        query = "SELECT * FROM employees WHERE YEAR(date_of_joining) = 2021"
        cursor.execute(query)
        employees = cursor.fetchall()
        
        # Write employees data to CSV file
        with open("employees_2001.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Employee ID", "Email", "Name", "Phone", "PF ID", "Date of Joining", "Date of Birth", "Department"])
            writer.writerows(employees)
        
        print("Employees joined in 2001 written to employees_2021.csv file.")
        
        

        
employee = Employee("130", "abc xyz", "xyz@example.com", "8907654321", "480", "2021-01-01", "2001-03-31", "IT")
employee.add_employee()
Employee.employees_joined_in_2021_to_csv()
Employee.update_employee_phone(124)


