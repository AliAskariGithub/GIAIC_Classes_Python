import random
print("\n -------------------------------- This is the Program for Rolling Dice --------------------------------")

NUM_SIDES : int = 6
def main():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total : int = die1 + die2
    
    print(f"\n\t Dice have {NUM_SIDES} sides each")
    print(f"\n\t First die: {die1}")
    print(f"\n\t Second die: {die2}")
    
    print(f"\n\t Total of two dice is: {total}")
    
if __name__ == '__main__':
    main()
    
print("\n -------------------------------- Thank you for using the Program --------------------------------")