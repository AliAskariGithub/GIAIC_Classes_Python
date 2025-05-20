print("\n -------------------------------- This is the First 20 Even Numbers Program --------------------------------")

def print_even_numbers(count):
    for i in range(count):
        print(i * 2)

def main():
    NUMBER_COUNT = 20
    print(f"\nPrinting first {NUMBER_COUNT} even numbers:\n")
    print_even_numbers(NUMBER_COUNT)

if __name__ == '__main__':
    main()

print("\n -------------------------------- Thank you for using program  --------------------------------")