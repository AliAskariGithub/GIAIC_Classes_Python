class Engine:
    def start(self):
        return "Engine starting..."

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start_car(self):
        return self.engine.start()

# Example usage
if __name__ == "__main__":
    car = Car()
    print(car.start_car())