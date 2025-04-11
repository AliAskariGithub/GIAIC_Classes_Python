print("\n -------------------------------- This is the Program to Calculate Energy --------------------------------")

speed_of_light = 299792458

def main():
    mass = float(input("\n\t Enter the mass in kilogram(kg): "))
    print("\n\t energy = mass * speed of light ^ 2")
    print(f"\n\t mass = {str(mass)}kg")
    print(f"\n\t speed of light = {str(speed_of_light)} m/s")
    energy =  mass * (speed_of_light ** 2)
    print(f"\n\t {str(energy)} joules of energy")
    
if __name__ == '__main__':
    main()
    
print("\n -------------------------------- Thank you for using the Program --------------------------------")