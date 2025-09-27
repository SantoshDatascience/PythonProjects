import os

class UtilityFunction:
    @staticmethod
    def ClearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')

class EmployeeRepository:
    def __init__(self):
        self.employees = {
            101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 500000}
        }
        self.next_emp_id = max(self.employees.keys()) + 1 if self.employees else 1

    def add_employee(self, name, age, department, salary):
        self.employees[self.next_emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }
        emp_id = self.next_emp_id
        self.next_emp_id += 1
        return emp_id

    def get_all_employees(self):
        return self.employees

    def search_employee(self, emp_id):
        return self.employees.get(emp_id)

class EmployeeService:
    def __init__(self, employee_repository):
        self.employee_repository = employee_repository

    def add_employee(self):
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        department = input("Enter employee department: ")
        salary = float(input("Enter employee salary: "))
        emp_id = self.employee_repository.add_employee(name, age, department, salary)
        print(f"Employee added successfully with ID: {emp_id}")

    def view_all_employees(self):
        employees = self.employee_repository.get_all_employees()
        if employees:
            for emp_id, emp in employees.items():
                print(f"ID: {emp_id}, Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}, Salary: {emp['salary']}")
        else:
            print("No employee records found.")

    def search_employee(self):
        search_id = int(input("Enter employee ID to search: "))
        emp = self.employee_repository.search_employee(search_id)
        if emp:
            print(f"Employee Found: ID: {search_id}, Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}, Salary: {emp['salary']}")
        else:
            print("Employee not found.")

class Menu:
    def __init__(self, employee_service):
        self.employee_service = employee_service

    def show_menu(self):
        while True:
            UtilityFunction.ClearScreen()
            print("\n=== Employee Management System ===")
            print("1. Add Employee")
            print("2. View All Employees")
            print("3. Search for Employee")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                # Add Employee
                self.employee_service.add_employee()
                input("Press Enter to continue...")
            elif choice == "2":
                # View All Employee
                self.employee_service.view_all_employees()
                input("Press Enter to continue...")
            elif choice == "3":
                # Search Employee
                self.employee_service.search_employee()
                input("Press Enter to continue...")
            elif choice == "4":
                # Exit Program
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Enter number between 1 to 4.")
                input("Press Enter to continue...")

# Entry 
employee_repository = EmployeeRepository()
employee_service = EmployeeService(employee_repository)
menu = Menu(employee_service)
menu.show_menu()
