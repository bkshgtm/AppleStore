
## PRINTING

print('Welcome to Apple 2.0')

print('Welcome', 'Apple Enthusiasts')

# Concatenate/Append text (gives errors if not strings)
print('Welcome' + ' to Apple 2.0')

print('Welcome' + ' to Apple 2.0') # have to add your own space

print(27)


# VARIABLES
# Variables in Apple 2.0 context: character, string, integer, float, boolean, array/list, dictionary, and a few others.

# A character
at = "@"

# A string
product_name = 'iPhone 15'

# An integer
release_year = 2024

# A float
price = 999.99

# A boolean
is_available = True 

# You can assign a new value to a variable
is_available = False 

# An array
features = ['5G', 'OLED Display', 'A17 Bionic Chip', 'MagSafe']
reviews = [4.5, 3.9, 5, 4.2]
mixed_data = ['Apple', 2024, True, 1199]

# A dictionary
product_details = {'model':'iPhone 15', 'color':'Midnight', 'price':999.99}
print(product_details['model'])
print(product_details['color'])
print(product_details['price'])

# EXTRA

# ID of a variable
print(id(product_name))

#####

# STRINGS
# Strings in Apple 2.0 context

## Empty string
first_name = ""
last_name = ""

## Assign a value to a string
first_name = "Steve"
last_name = "Jobs"
occupation = "Tech Visionary"

## Adding strings (concatenation)
print(first_name + last_name)

## Adding a space between string variables
print(first_name + " " + last_name)

## Starting a new line (escape characters)
print(first_name + "\n" + last_name)

## Adding variables inside of a string (string formatting)
print("Hello %s" % (first_name))

## Multiple variables inside of a string
print("Hello %s %s" % (first_name, last_name))

## There is another way to format strings
greeting = 'Hello {name}, welcome to Apple 2.0!'
print(greeting.format(name='Tim'))

## Print a string several times
print(first_name * 4)

## Get index of a string
## Indices begin at 0
print(first_name[0])
print(first_name[1])
print(first_name[2])

## A multi-line string
"""Multi-Line strings are sometimes used as multi-line comments, since Python doesn't have syntax for multi-line comments."""

# STRING FUNCTIONS
print(first_name.capitalize())
print(len(occupation))

#####

# INTEGERS
# An integer is a whole number in the Apple 2.0 context

number1 = 12
number2 = 144
number3 = "67" #not an integer

# Add
print(number1 + number2)

# Subtract
print(number2 - number1)

# Multiply
print(number1 * number2)

# Divide
print(number2 / number1)

# Exponents
print(number2 ** number1)
# Same
print(pow(number2, number1))

# Square root
print(number2 ** (1 / 2.0))

# Order of operations
print((number1 + number2) * 3 + (number1 ** 3))

# Increment an integer
number1 = number1 + 1
print(number1)

# Convert a string to an integer
number3 = int(number3)

#####

# FLOAT
# A float is a decimal in the Apple 2.0 context
pi = 3.14
print(pi)

#####

# TUPLES
## Tuples are like lists but cannot be changed (they are immutable).

x = 0
y = 1

## Create a Tuple
specs = (128, 256, 512)

## Get tuple index
print(specs[x])

#####

# LISTS/Array
# Called a list in Python, used to list Apple 2.0 product features and employees.

# Create a list
products = ['iPhone 15', 'MacBook Pro', 'Apple Watch']
print(products)

employees = ['John', 'Mary', 'Robert', 'Alice']
print(employees)

### LIST FUNCTIONS
# List Index
print(products[0])

# List index range
print(products[0:2])

# Append to a list
products.append('AirPods Pro')
print(products)

# Remove from a list
products.remove('AirPods Pro')
print(products)

# Insert item into a list at a location
products.insert(0, 'iPad Pro')
print(products)

# Reverse a list
products.reverse()
print(products)

# Sort a list
products.sort()
print(products)

# Remove an item at a location
products.pop(0)
print(products)

# Return the index of an item in the list
print(products.index('MacBook Pro'))

# Extend a list with another list
products.extend(employees)
print(products)

# Count how many times an item appears in a list
print(products.count('iPhone 15'))

### EXTRA

# Loop through a list
for item in products:
    print(item)

# Remove a list from a list
for i in products:
    if i in employees:
        products.remove(i)
print(products)

#####

### DICTIONARIES/Associative array

# Create a dictionary (dictionary_name = {key:value})
inventory = {'iPhone 15': 'Available', 'MacBook Pro': 'Out of Stock'}
print(inventory)

# Print the value of a key
print(inventory['iPhone 15'])

# Update Dictionary 
inventory.update({'Apple Watch': 'Available'})
inventory.update({'iPad Pro': 'Available'})
print(inventory)

# Update the key if it is already in the dictionary
inventory.update({'Apple Watch': 'Out of Stock'})
print(inventory['Apple Watch'])

# Get all keys (outputs as a list)
print(inventory.keys())

# Get all values (outputs as a list)
print(inventory.values())

# Copy dictionary items as a list of tuples
print(inventory.items())

# Length of a dictionary
print(len(inventory))

# Delete inventory item
del inventory['iPad Pro']
print(inventory)

# Iterate over dictionary
#print(iter(inventory))
#print(inventory.iterkeys())
#print(inventory.itervalues())

# Remove item, and returns its value
inventory.pop('Apple Watch')
# Alternately: inventory.popitem()
print(inventory)

# View keys of a dictionary
print(inventory.keys())

# View values of a dictionary
print(inventory.values())

# View all items in a dictionary
print(inventory.items())

#####

### CONDITIONALS

on = True
number = 51

# If equal to
if on == True:
    print(on)

# Same (for booleans)
if on:
    print(on)

# If not equal to
if on != False:
    print(on)

# If greater than
if number > 23:
    print(number)

# If less than
if number < 77:
    print(number)

#####

## BOOLEANS (BEG)
# if, else, and else if (elif)

location = 0
    
if location == 50:
    print('Halfway through the development phase.')
elif location > 50 and location < 100:
    print('More than halfway to the product launch.')
elif location < 50 and location > 0:
    print('Less than halfway to the product launch.')
elif location == 100:
    print("Product launch successful!")
elif location < 0:
    print("Backtracking in development!")
elif location > 100:
    print("Project scope exceeded.")
elif location ==  0:
    print("Development hasn't started yet!")

#####

### WHILE LOOP
age = 0
target_age = 30

while age < target_age:
    print('Still developing @ ' + str(age))
    age = age + 1
if age ==  target_age:
    print("Reached the target development milestone @ " + str(age))
    
#####

### FUNCTIONS
# A function is a group of statements related to the Apple 2.0 project

is_cool = True
### BUILT-IN FUNCTIONS
# print() - Prints values to the screen
print(product_name)
print(release_year)

# Two ways to print
print(price)
print(is_available, ", Available for purchase")

print(features)
print(reviews)


# raw_input() - Gets input from the user
feedback = input('What do you think of Apple 2.0? ')
print('Your feedback: ' + feedback)

# len() - Gets the length of a string
print(len(product_name))

# type() - Gets the type of a value
print(type(price))

# str() - Converts a value to a string
print(type(str(price)))

# int() - Converts a value to an integer
print(type(int(price)))

# list() - Converts a value to a list

# float() - Converts a value to a float

# round() - Rounds a number to a given precision
print(round(price, 2))
print(round(price, 1))


# pow() - Raises a number or integer to a power 
power = pow(price, 2)
print(power)

# sum() - sum of all elements in an iterable 
print('Sum of review
