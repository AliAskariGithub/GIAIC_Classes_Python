class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} car is starting"

# Example usage
if __name__ == "__main__":
    car = Car("Toyota")
    print(car.brand)
    print(car.start())