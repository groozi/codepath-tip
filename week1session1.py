# Breakout Room Problems for Week 1 Session 1: Group 35

def divider():
    print("\n˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜\n")

# Standard Problem Set Version 1 BELOW:
divider()
print("Standard Problem Set Version 1:\n")
divider()

print("Problem 1: \n")
# Problem 1: Hundred Acre Wood
#   Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".

def welcome():
    print("Welcome to The Hundred Acre Wood!")

welcome()

print("\nProblem 2: \n")
# Problem 2: Greeting
#       Write a function greeting() that accepts a single parameter, a string name, 
#       and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

greeting("Graziella")

print("\nProblem 3: \n")
# Problem 3: Catchphrase 
#   Write a function print_catchphrase() that accepts a string character as a parameter
#   and prints the catchphrase of the given character as outlined in the table below.

#   Character	Catchphrase
#       "Pooh"	            "Oh bother!"
#       "Tigger"	        "TTFN: Ta-ta for now!"
#       "Eeyore"	        "Thanks for noticing me."
#       "Christopher Robin"	"Silly old bear."

#   If the given character does not match one of the characters included above, print 
#   "Sorry! I don't know <character>'s catchphrase!"

def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

print_catchphrase("Graziella")
print_catchphrase("Tigger")
print_catchphrase("pooh")
print_catchphrase("Eeyore")

print("\nProblem 4: \n")
# Problem 4: Return Item
#   Implement a function get_item() that accepts a 0-indexed list items 
#   and a non-negative integer x and returns the element at index x in items. 
#   If x is not a valid index of items, return None.

def get_item(items, x):
    if x <= len(items):
        print(items[x]) 

    else:
        print("None")

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)

print("\nProblem 5: \n")
# Problem 5: Total Honey
#   Winnie the Pooh wants to know how much honey he has. 
#   Write a function sum_honey() that accepts a list of integers 
#   hunny_jars and returns the sum of all elements in the list. 
#   Do not use the built-in function sum().

def sum_honey(hunny_jars):
    sum = 0

    for jar in hunny_jars:
        sum += jar
    print(sum)

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)

print("\nProblem 6: \n")
# Problem 6: Double Trouble
#   Help Winnie the Pooh double his honey! Write a function doubled() 
#   that accepts a list of integers hunny_jars as a parameter and 
#   multiplies each element in the list by two. Return the doubled list.

def doubled(hunny_jars):
    for i in range(len(hunny_jars)):
        hunny_jars[i] *= 2
    print(hunny_jars)

hunny_jars = [1, 2, 3]
doubled(hunny_jars)

print("\nProblem 7: \n")
# Problem 7: Poohsticks
#   Winnie the Pooh and his friends are playing a game called Poohsticks 
#   where they drop sticks in a stream and race them. They time how long it takes 
#   each player's stick to float under Poohsticks Bridge to score each round.

#   Write a function count_less_than() to help Pooh and his friends determine 
#   how many players should move on to the next round of Poohsticks. 
#   count_less_than() should accept a list of integers race_times and an 
#   integer threshold and return the number of race times less than threshold.

def count_less_than(race_times, threshold):
    count = 0

    for i in range(len(race_times)):
        if race_times[i] < threshold:
            count += 1

    print(count)

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)

print("\nProblem 8: \n")
# Problem 8: Pooh's To Do's
#   Write a function print_todo_list() that accepts a list 
#   of strings named tasks. The function should then number 
#   and print each task on a new line using the format:
    #   Pooh's To Dos:
    #       1. Task 1
    #       2. Task 2
    #       ...

def print_todo_list(tasks):

    print("Pooh's To Dos:")

    for i in range(len(tasks)):
        print(f"{i + 1}. Task {i + 1}")

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)
print()

task = []
print_todo_list(task)
   
print("\nProblem 9: \n")
# Problem 9: Pairs
#   Rabbit is very particular about his belongings and 
#   wants to own an even number of each thing he owns. 
#   Write a function can_pair() that accepts a list of 
#   integers item_quantities. Return True if each number 
#   in item_quantities is even. Return False otherwise.

def can_pair(item_quantities):
    boolean_flag = True

    for i in range(len(item_quantities)):
        if item_quantities[i] % 2 == 1 :
            boolean_flag = False

    print(boolean_flag)

item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities)

print("\nProblem 10: \n")
# Problem 10: Split Haycorns
#   Piglet has collected a big pile of his favorite food, 
#   haycorns, and wants to split them evenly amongst his friends. 
#   Write a function split_haycorns() to help Piglet determine the 
#   number of ways he can split his haycorns into even groups. 
#   split_haycorns() accepts a positive integer quantity as a parameter 
#   and returns a list of all divisors of quantity.

def split_haycorns(quantity):
    result_list = []

    for i in range(quantity):
        if quantity % (i + 1) == 0:
            result_list.append(i + 1)
    
    print(result_list)

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)

quantity = 5
split_haycorns(quantity)

print("\nProblem 11: \n")
# Problem 11: T-I-Double Guh-ER
#   Signs in the Hundred Acre Wood have been losing letters as 
#   Tigger bounces around stealing any letters he needs to spell 
#   out his name. Write a function tiggerfy() that accepts a string 
#   s, and returns a new string with the letters t, i, g, e, and r from it.

def tiggerfy(s):
    print(f'"{s.translate({ord(i): None for i in 'tigerTIGER'})}"')

s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)

print("\nProblem 12: \n")
# Problem 12: Thistle Hunt
#   Pooh, Piglet, and Roo are looking for thistles to 
#   gift their friend Eeyore. Write a function locate_thistles() 
#   that takes in a list of strings items and returns a list of 
#   the indices of any elements with value "thistle". The indices 
#   in the resulting list should be ordered from least to greatest.

def locate_thistles(items):
    list = []

    for i in range(len(items)):
        if items[i] == "thistle":
            list.append(i)
    
    print(list)

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)

# Standard Problem Set Version 2 BELOW:
divider()
print("Standard Problem Set Version 2:\n")
divider()

# Problem 1: Batman
# Write a function batman() that prints the string "I am vengeance. I am the night. I am Batman!".

def batman():
    print("I am vengeance. I am the night. I am Batman!\n")

batman()

# Problem 2: Mad Libs
#   Write a function madlib() that accepts one parameter, 
#   a string verb. The function should print the sentence: 
#   "I have one power. I never <verb>. - Batman".

def madlib(verb):
    print(f"I have one power. I never {verb}. - Batman")

verb = "give up"
madlib(verb)

verb = "nap"
madlib(verb)
print()

# Problem 3: Trilogy
#   Write a function trilogy() that accepts an integer 
#   year and prints the title of the Batman trilogy movie 
#   released that year as outlined below.
#       Year	Movie Title
#       2005	"Batman Begins"
#       2008	"The Dark Knight"
#       2012	"The Dark Knight Rises"

def trilogy(year):
    if year == 2005:
        print("Batman Begins")
    elif year == 2008:
        print("The Dark Knight")
    elif year == 2012:
        print("The Dark Knight Rises")
    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}.")

year = 2008 
trilogy(year)

year = 1998
trilogy(year)
print()

# Problem 4: Last
#   Implement a function get_last() that accepts 
#   a list of items items and returns the last item 
#   in the list. If the list is empty, return None.

def get_last(items):
    if len(items) > 0:
        print(items[len(items) - 1])
    else:
        print("None")

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)
print()

# Problem 5: Concatenate
#   Write a function concatenate() that takes in 
#   a list of strings words and returns a string 
#   concatenated that concatenates all elements in words.

def concatenate(words):
    joined = "".join(words)
    print(joined)

words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)
print()

# Problem 6: Squared
#   Write a function squared() that accepts a 
#   list of integers numbers as a parameter and 
#   squares each item in the list. Return the squared list.

def squared(numbers):
    for i in range(len(numbers)):
        numbers[i] *= numbers[i]
    print(numbers)

numbers = [1, 2, 3]
squared(numbers)
print()

# Problem 7: NaNaNa Batman!
#   Write a function nanana_batman() that accepts 
#   an integer x and prints the string "nanana batman!" 
#   where "na" is repeated x times. Do not use the * operator.

def nanana_batman(x):
    for i in range(x):
        print("na", end="")
    print(" batman!")

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)
print()

# Problem 8: Find the Villian
#   Write a function find_villain() that accepts 
#   a list crowd and a value villain as parameters 
#   and returns a list of all indices where the villain 
#   is found hiding in the crowd.

# def find_villian(crowd, villain):

