print("\n -------------------------------- This is the Fibonacci Sequence Generator Program --------------------------------")

def generate_fibonacci(max_value):
    current = 0
    next = 1
    
    while current <= max_value:
        print(current)
        temp = current + next
        current = next
        next = temp

def main():
    MAX_VALUE = 10000
    print(f"\nGenerating Fibonacci sequence up to {MAX_VALUE}:\n")
    generate_fibonacci(MAX_VALUE)

if __name__ == '__main__':
    main()

print("\n -------------------------------- Thank you for using program --------------------------------")