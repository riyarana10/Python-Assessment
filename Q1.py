import mysql.connector
import csv
import re   

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
        
     def open_connection(self):
         conn = mysql.connector.connect(host='localhost', password='Password1!',user='root', database='test')
         if conn.is_connected():
             print("connection established")
         return conn
    
     def add_employee(self):
        conn = self.open_connection()
        
        emp_id = input("enter employee id: ")
        emp_name = input("enter employee name: ")
        email = input("enter employee email: ")
        phone = input("enter employee phone: ")
        PF_id = input("enter employee pf id: ")
        date_of_joining = input("enter employee date of joining: ")
        dob = input("enter dob of employee: ")
        department = input("enter department of emoloyee: ")
        
        if not self.is_employee_id_unique(emp_id):
            print("Employee ID already exists. Please try again.")
            return
        
        if not self.check_email(email):
            print("Invalid email format. Please try again.")
            return
        
        if not self.is_valid_phone_number(phone):
            print("Invalid phone number format. Please try again.")
            return

        cursor = conn.cursor()
        query = "INSERT INTO employees (emp_id, emp_name, email, phone, PF_id, date_of_joining, dob, department) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (emp_id, emp_name, email, phone, PF_id, date_of_joining,dob, department)
        cursor.execute(query, values)
        
        conn.commit()
        print("Employee added successfully.")
        
        conn.close()
     
     
     def show_employee_list(self):
        conn = self.open_connection()
        query = '''
        SELECT * FROM employees
        '''
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
     def update_employee_phone(self):
        conn = self.open_connection()
        emp_id = input("enter employee id to update phone number")
        query = '''
        SELECT * FROM employees WHERE emp_id = %s
        '''
        cursor = conn.cursor()
        cursor.execute(query, (emp_id,))
        employee = cursor.fetchone()

        if employee:
            phone = input("Enter the new phone number: ")
            if self.is_valid_phone_number(phone):
                query = '''
                UPDATE employees
                SET phone = %s
                WHERE emp_id = %s
                '''
                values = (phone, emp_id)
                cursor.execute(query, values)
                conn.commit()
                conn.close()
                print("Phone number updated successfully!")
            else:
                print("Invalid phone number!")
        else:
            print("Employee not found!")
         
     def delete_employee(self):
        conn = self.open_connection()
        emp_id = input("enter employee id")
        query = '''
        SELECT * FROM employees WHERE emp_id = %s
        '''
        cursor = conn.cursor()
        cursor.execute(query, (emp_id,))
        employee = cursor.fetchone()
        if employee:
                query = '''
                DELETE FROM employees
                WHERE emp_id = %s
                '''
                values = (emp_id,)
                cursor.execute(query,values)
                conn.commit()
                conn.close()
                print("employee deleted successfully!")
        else:
            print("Employee not found!")
        

    
     def is_employee_id_unique(self,emp_id):
        conn = self.open_connection()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM employees WHERE emp_id = %s"
        cursor.execute(query, (emp_id,))
        count = cursor.fetchone()[0]
        conn.close()
        return count == 0
        
     
     def check_email(self,email):
        email = str(email)
        regex = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
        if re.fullmatch(regex, email):
            return True
        else:
            return False
    
    
     def is_valid_phone_number(self,phone):
         if len(phone) < 10 or not phone.isdigit():
             return False
         return True
     
     
     def employees_joined_in_2021_to_csv(self):
        conn = self.open_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM employees WHERE YEAR(date_of_joining) = 2021"
        cursor.execute(query)
        employees = cursor.fetchall()
        conn.close()
        
        # Write employees data to CSV file
        with open("employees_2001.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Employee ID", "Email", "Name", "Phone", "PF ID", "Date of Joining", "Date of Birth", "Department"])
            writer.writerows(employees)
        
        print("Employees joined in 2001 written to employees_2021.csv file.")
        
def application():
    print("enter 1 to add employee: ") 
    print("enter 2 to read employee list: ")
    print("enter 3 to update employee's phone number: ")    
    print("enter 4 to delete employee: ")
    
    employee = Employee()
    x = input("enter choice")
    if(x == '1'): employee.add_employee()
    elif(x == '2'): 
        emp_list = employee.show_employee_list()
        print(emp_list)
    elif(x == '3'): employee.update_employee_phone()
    else: employee.delete_employee()


application()
