def main():
    numbers = {}
    
    while True:
        user_input = input("Enter a number: ")
        
        if user_input == "":
            break
            
        num = int(user_input)
        
        if num in numbers:
            numbers[num] += 1
        else:
            numbers[num] = 1
    
    for number, count in numbers.items():
        print(f"{number} appears {count} times.")

if __name__ == '__main__':
    main()