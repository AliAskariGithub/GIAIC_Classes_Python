# **All work will be done on Google Colab not in VSCode or anyother IDE**

"""
- Igoner these prints
- This is for Spacing while printing the program

print()
print("-" * 96)
print()

"""


# List Concept
sehari_items: list = ["Parhata", "Chai", "Lassi", "Pani", "Pheni"]
sehari_items.pop(1)  # "Chai" will be removed
sehari_items.append("Nihari")  # "Nihari" will be added
sehari_items.remove("Parhata")  # "Parhata" will be removed
print(sehari_items)

print()
print("-" * 96)
print()

# Tuple Concept
sehari_items_tuple = ("Pani", "Chai", "Salan")
# sehari_items_tuple[1] = "Lassi"  # Throws an error because tuples are immutable
print(sehari_items_tuple)

print()
print("-" * 96)
print()

# Set Concept
""" Sets are Unordered, Mutable, and Do Not Allow Duplicates """
iftar_items: set = {"Pakoray", "khunjoor", "Rooh Afza", "Furit Chat", "Rooh Afza", "Water"}
iftar_items.add("Fruit Chat")  # Typo fixed, but sets do not allow duplicates
iftar_items.remove("Water")  # "Water" will be removed
# iftar_items[2]  # Throws an error because sets do not support indexing
print(iftar_items)

print()
print("-" * 96)
print()

# Frozenset Concept
""" Frozensets are Unordered, Immutable, and Do Not Allow Changes """
iftar_items_frozenset: frozenset = frozenset(iftar_items)
# iftar_items_frozenset.add("Tea")  # Throws an error because frozensets are immutable
print(iftar_items_frozenset)

print()
print("-" * 96)
print()

# Input Concept
user_name = input("Enter your name: ")
print("Hi there, my name is", user_name)

print()

addition = input("Enter a number: ")
# sum = 10 + addition  # Throws a TypeError because input is a string
sum_result = 10 + int(addition)
print("Your result is:", sum_result)

print()

# Converting list to tuple
fixing_sheri_items: list = ["Parhata", "Chai", "Lassi", "Pani", "Pheni"]
fixed_sheri_items = tuple(fixing_sheri_items)
print("Fixed items:", fixed_sheri_items)

# Removing duplicates using a set
make_unique_sehari_items: list = ["Parhata", "Chai", "Lassi", "Pani", "Pheni", "Chai", "Lassi"]
print("Unique items:", make_unique_sehari_items)

unique_sheri_items: set = set(make_unique_sehari_items)
print("Removed duplicates from unique items:", unique_sheri_items)

more_sheri_items: list = list(unique_sheri_items)
print("Listed items:", more_sheri_items)

print()
print("-" * 96)
print()

# Implementing Type Casting Concept
num01: int = 10
num02: float = 3.5

sum_result = num01 + num02
print("Type of num02:", type(num02))

div = num02 / num02
print("Type of division result:", type(div))

num = "20"
print("Type after casting to int:", type(int(num)))

print()
print("-" * 96)
print()

# Def (Function) Concept
def greeting(name: str) -> None:
    print(f"Assalam-u-Alikum, {name}")

greeting("Ali")

print()

def sandwich_buddy(bread: str, filling: str) -> str:
    sandwich_bread = f"{bread} Bread"
    sandwich_filling = f"{filling} Filling"

    completed_sandwich = f"Your sandwich with {sandwich_bread} and {sandwich_filling} is ready to be served!"

    return completed_sandwich

ali_sandwich = sandwich_buddy("Garlic", "Beef Patty")
print("Ali:", ali_sandwich)
fatima_sandwich = sandwich_buddy("Simple", "Chicken Patty")
print("Fatima:", fatima_sandwich)

print()
print("-" * 96)
print()

# Module Concept
import math
import random
# from math import sqrt

value = math.sqrt(81)
print("The square root of 81 is:", value)

print("Random number between 1 and 10:", random.randint(1, 10))

import requests

response = requests.get("https://api.github.com")
print("GitHub API Response:", response)