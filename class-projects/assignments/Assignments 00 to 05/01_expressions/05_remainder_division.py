print("\n -------------------------------- This is the Program for Remainder Division --------------------------------")

def main():
    dividend : float = float(input("\n\t Please enter an integer to be divided: "))
    divisor : float = float(input("\n\t Please enter an integer to divide by: "))
    
    quotient : float = dividend // divisor
    remainder : float = dividend % divisor
    
    print(f"\n\t The result of this division is {quotient} with a remainder of {remainder}")
    
    
if __name__ == '__main__':
    main()
    
print("\n -------------------------------- Thank you for using the Program --------------------------------")