print("\n -------------------------------- This is the Program to Calculate the Perimeter of a Triangle --------------------------------")

def main():
    side1 : float = (float(input("\n\t What is the length of side 1: ")))
    side2 : float = (float(input("\n\t What is the length of side 2: ")))
    side3 : float = (float(input("\n\t What is the length of side 3: ")))
    
    perimeter = side1 + side2 + side3
    print(f"\n\n\t The perimeter of the triangle is {perimeter}")

if __name__ == '__main__':
    main()
    
print("\n -------------------------------- Thank you for using the Program --------------------------------")