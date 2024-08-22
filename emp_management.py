import mysql.connector

# Establishing a connection to the database
try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    mycr = mydb.cursor()
    mycr.execute("use tasks ")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

class EmpManagement:
    def list_details(self):
        try:
            mycr.execute("select * from emp_details")
            for i in mycr:
                print(f''' ----------------------------------    
                    Id = {i[0]}
                    Name = {i[1]}
                    Age = {i[2]}
                    Salary = {i[3]}
                ''')
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def add_details(self, id, name, age, salary):
        try:
            query = "insert into emp_details(id,name,age,salary) values(%s,%s,%s,%s)"
            values = (id, name, age, salary)
            mycr.execute(query, values)
            mydb.commit()
            print("\n Data added successfully \n")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def edit_details(self, id, field, value):
        try:
            if field == 'age' or field == 'salary':
                value = int(value)
            query = f"update emp_details set {field} = %s where id = %s"
            values = (value, id)
            mycr.execute(query, values)
            mydb.commit()
            print("\n Value changed successfully \n")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        except ValueError:
            print("\n Invalid value for age or salary. Please enter a valid integer.\n")
    
    def delete_details(self, id):
        try:
            mycr.execute("delete from emp_details where id = %s", (id,))
            mydb.commit()
            print("\n Data deleted successfully \n")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

# Creating an instance of the EmpManagement class
obj1 = EmpManagement()

# Main menu loop
choice = 0
while choice != 5:
    print("-----------MENU---------------")
    print('''Please select your input
          1 - List
          2 - Add
          3 - Edit
          4 - Delete
          5 - Exit''')
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("\n Invalid choice. Please enter a number between 1 and 5.\n")
        continue
    
    if choice == 1:
        obj1.list_details()
    elif choice == 2:
        try:
            id = int(input("Enter the id: "))
            name = input("Enter the name: ")
            age = int(input("Enter the age: "))
            salary = int(input("Enter the salary: "))
            obj1.add_details(id, name, age, salary)
        except ValueError:
            print("\n Invalid input. Please enter valid data.\n")
    elif choice == 3:
        try:
            id = int(input("Enter the id: "))
            field = input("Which field do you want to edit: ")
            value = input("Enter the value: ")
            obj1.edit_details(id, field, value)
        except ValueError:
            print("\n Invalid input. Please enter valid data.\n")
    elif choice == 4:
        try:
            id = int(input("Enter the id: "))
            obj1.delete_details(id)
        except ValueError:
            print("\n Invalid id. Please enter a valid integer.\n")
    elif choice == 5:
        break
    else:
        print("\n Invalid choice. Please select a number between 1 and 5.\n")
