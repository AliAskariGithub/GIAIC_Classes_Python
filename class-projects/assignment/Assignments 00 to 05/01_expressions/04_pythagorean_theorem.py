import math
print("\n -------------------------------- This is the Program to Calculate the Hypotenuse of a Right Triangle --------------------------------")

def main():
    ab : float = float(input("\n\t Enter the length of the side ab: "))
    bc : float = float(input("\n\t Enter the length of side bc: "))
    hypotenuse : float = math.sqrt(ab**2 + bc**2)
    print(f"\n\t The length of bc (the hypotenuse) is: {hypotenuse:.2f} ")
    
if __name__ == '__main__':
    main()
    
print("\n -------------------------------- Thank you for using the Program --------------------------------")