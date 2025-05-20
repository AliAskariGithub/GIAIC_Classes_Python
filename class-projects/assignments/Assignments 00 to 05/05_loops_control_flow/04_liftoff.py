print("\n -------------------------------- This is the Rocket Launch Countdown Program --------------------------------")

def countdown():
    for i in range(10):
        print(10 - i)
    print("Liftoff!")

def main():
    print("\nInitiating launch sequence...\n")
    countdown()

if __name__ == '__main__':
    main()

print("\n -------------------------------- Thank you for using program --------------------------------")