import random
print("\n -------------------------------- This is the Program to Simulate the Dice  --------------------------------")

NUM_SIDES = 5

def roll_dice():
    die1 : int = random.randint(1, NUM_SIDES)
    die2 : int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("\n\t Total of two dice:", total)

def main():
    die1 : int = 10
    print(f"\n ----------- die1 in main() starts as: {die1} -----------")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f" ----------- die1 in main() starts as: {die1} ----------- " )
    
if __name__ == '__main__':
    main()
    
print("\n -------------------------------- Thank you for using the Program --------------------------------")