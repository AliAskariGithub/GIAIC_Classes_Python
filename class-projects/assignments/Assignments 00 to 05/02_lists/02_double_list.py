print("\n -------------------------------- This is the Program to add many numbers  --------------------------------")

def main():
    numbers : list[int] = [1, 2, 3, 4, 5]
    for i in range(len(numbers)):
        elem_at_index = numbers[i]
        numbers[i] = elem_at_index * 2
        
    print("\n\t", numbers)
    
    
if __name__ == '__main__':
    main()
    
print("\n -------------------------------- Thank you for using the Program --------------------------------") 