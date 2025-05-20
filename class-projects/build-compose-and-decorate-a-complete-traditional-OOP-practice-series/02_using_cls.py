class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        return f"Total objects created: {cls.count}"

# Example usage
if __name__ == "__main__":
    c1 = Counter()
    c2 = Counter()
    print(Counter.display_count())