#python lists and their manupulation
import random

states = ["Delaware", "New York", "California"]
states.append("Valaofland") #adds an item from the last
states.extend(["vaatpata", "ampata", "kolapata"]) #extens the list
# print(len(states))
# todo: print random names from the list
names = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "George", "Hannah",
         "Isaac", "James", "Katherine", "Leo", "Mary", "Noah", "Olivia", "Peter",
         "Quinn", "Robert", "Sarah", "Thomas", "Umaima", "Victor", "William", "Xavier",
         "Yusuf", "Zara"]
random_name = random.randint(0, len(names)-1)
print(names[random_name])

