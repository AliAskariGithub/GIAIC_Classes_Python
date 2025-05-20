class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public
        self._salary = salary     # protected
        self.__ssn = ssn         # private
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

# Example usage
if __name__ == "__main__":
    emp = Employee("John", 50000, "123-45-6789")
    print(emp.name)         # Works
    print(emp._salary)      # Works but shouldn't be accessed
    # print(emp.__ssn)     # Will raise AttributeError