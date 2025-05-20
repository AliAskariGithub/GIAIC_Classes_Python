print("\n -------------------------------- This is the Program    --------------------------------")

MINIMUM_HEIGHT : int = 50

def main():
    heigth = float(input("How tall are you "))
    
    if(heigth >= MINIMUM_HEIGHT):
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


if __name__ == '__main__':
    main()
    
print("\n -------------------------------- Thank you for using the Program --------------------------------")