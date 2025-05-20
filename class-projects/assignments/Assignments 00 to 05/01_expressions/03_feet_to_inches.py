print("\n -------------------------------- This is the Program to Convert Feet to Inches --------------------------------")

INCHES_IN_FOOT: int = 12

def main():
    feet : float = float(input("\n\t Enter number of feet: "))
    inches : float = feet * INCHES_IN_FOOT
    print(f"\n\t That is {inches} inches.")
    
if __name__ == '__main__':
    main()
    
print("\n -------------------------------- Thank you for using the Program --------------------------------")