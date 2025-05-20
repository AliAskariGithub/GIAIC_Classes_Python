class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)

# Example usage
if __name__ == "__main__":
    emp = Employee("John")
    dept = Department()
    dept.add_employee(emp)