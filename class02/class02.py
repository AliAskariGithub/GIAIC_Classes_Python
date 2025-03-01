"""
- Igoner these prints
- This is for Spacing while printing the program

print()
print("------------------------------------------------------")
print()

"""


# Split Concept
my_string : str = "Hello World"
modified_string : str = my_string.split("l")
print(modified_string)

print()
print("------------------------------------------------------")
print()

# Replace Concept
message : str = "Pakistan won all the matches of champions trophy!"
message : str = message.replace("Pakistan", "India")
print(message)

print()
print("------------------------------------------------------")
print()

# Join Concept
cricket_team : list = ", ".join(["Pakistan", "India", "USA"])
print("Teams: ", cricket_team)
print(type(cricket_team))

print()
print("------------------------------------------------------")
print()

# length Concept
my_name : str = "Ali Askari"
print("Name: ", my_name)
print("Name Length: ", len(my_name))

my_hobby : list = ["Games", "Anime", "Coding"]
print("Hobbies: ", my_hobby)
print("How many hobbies: ", len(my_hobby))

print()
print("------------------------------------------------------")
print()

# id Concept
your_fault : str = "Your fault is you are weak"
print(f"The id of this message *{your_fault}* is: ", id(your_fault))

print()
print("------------------------------------------------------")
print()


# System and Intern Concept
import sys

alpha : str = sys.intern("Hello User")
beta : str = sys.intern("Hello User!")
print(id(alpha))
print(id(beta))
print("Condition is: ", alpha is beta)


print()
print("------------------------------------------------------")
print()

# is Concept
a : str = "Hello User"
b : str = "Hello User"
print("Condition is: ", a is b)

c = "Hello "
d = "User"
print(c + d) 

print()
print("------------------------------------------------------")
print()

# List, splice, append, extend and pop Concept
furits : list = ["Mango", "Banana", "Cherry", "Grapes", "Apples"]
print("Furits list: ", furits)
print("Mentioned Furits: ", furits[0])
print("Mentioned Furits: ",furits[-1])

print("Splicing Furits: ", furits[0: -2])

furits.append("Orange") # It can add only one at a time
print("Appending Furits: ", furits)

furits.extend(["Kiwi", "Pineapple", "Dates"]) # It will add more than one
print("Extending Furits: ", furits)

furits.pop(5) # It will remove the word
print("Removing Furits: ", furits)

print()
print("------------------------------------------------------")
print()

# Dictonary Concept
person : dict = {
    #KEY     VALUE
    "name": "Ali Askari",
    "age": 16,
    "isStudent": True,
    "class": {
        "timing": "2PM to 5PM",
        "day": "Saturday"
    }
}

print("Person: ", person)
print("Student_Name: ", person["name"])
print("Student_Age: ", person["age"])
print("Student_Class: ", person["class"]["timing"])
print(f"Hi there my name is {person["name"]} and I am {person['age']} years old. And my class timing is {person['class']["day"]} {person['class']["timing"]} ")

print()
print("------------------------------------------------------")
print()

# Random Concept
import random
babar_azam : str = random.randint(0, 150)

if(babar_azam == 100):
    print("👑Full Century")
elif(babar_azam >= 50):
    print("🏏Half Century")
else:
    print("Loser🤬")

print()
print("------------------------------------------------------")
print()

# Tuples Concept
pak_circket_team = ("Babar Azam", "Rizwan", "Shaheen Afridi")
# pak_circket_team[1] = "Sarafraz Ahmed" # It will not change because it is Tuples
print("Player: ", pak_circket_team[2])

print()
print("------------------------------------------------------")
print()


# Sets Concept
values : set = {0, 1, 2, 3, 4, 2, 8}
print("Values: ", values)

furits : set = {"Mango", "Apple", "Grapes", "Banana"}
print("Furits: ", furits)

print()
print("------------------------------------------------------")
print()

# Filtering Concept and use these all data types by implementing one by one
filtering_method : str = dir(str)
print(filtering_method)