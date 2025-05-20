class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Example usage
if __name__ == "__main__":
    teacher = Teacher("Mr. Smith", "Mathematics")
    print(f"{teacher.name} teaches {teacher.subject}")