print("\n -------------------------------- This is the Program to Convert Fahrenheit to Celsius --------------------------------")

def main():
    degrees_fahrenheit = (float(input("\n\t Enter Temperature in Fahrenheit: ")))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    print(f"\n\t Temperature: {degrees_fahrenheit:.2f}F = {degrees_celsius:.2f}C")
    
    
if __name__ == '__main__':
    main()
    
print("\n -------------------------------- Thank you for using the Program --------------------------------")