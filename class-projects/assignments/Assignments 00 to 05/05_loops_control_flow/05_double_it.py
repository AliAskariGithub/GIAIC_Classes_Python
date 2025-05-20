print("\n -------------------------------- This is the Number Doubler Program Program --------------------------------")

def get_starting_number():
    while True:
        try:
            number = float(input("Enter a starting number: "))
            if number > 0:
                return number
            print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")

def double_until_hundred(start_value):
    curr_value = start_value
    while curr_value < 100:
        curr_value = curr_value * 2
        print(int(curr_value) if curr_value.is_integer() else curr_value)

def main():
    start_number = get_starting_number()
    print("\nDoubling sequence:")
    double_until_hundred(start_number)

if __name__ == '__main__':
    main()

print("\n -------------------------------- Thank you for using program --------------------------------")