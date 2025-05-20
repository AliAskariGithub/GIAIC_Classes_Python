# filepath: dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} the {self.breed} says: Woof!")

# Example usage
if __name__ == "__main__":
    dog = Dog("Max", "Golden Retriever")
    dog.bark()