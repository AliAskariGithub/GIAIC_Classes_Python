class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

# Example usage
if __name__ == "__main__":
    double = Multiplier(2)
    print(callable(double))
    print(double(5))