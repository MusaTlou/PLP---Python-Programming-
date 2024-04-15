# Understaning Variable

# # assign vlaue to site_name variable
# site_name = 'Power Learn Project'
# print(site_name)

# # assigning a new value to site_name variable
# site_name = 'apple.com'
# print(site_name)

# # assigning multiple values to multiple variables
# a, b, c, = 5, 3.2, 'Hello'
# print(a)
# print(b)
# print(c)

# # assign the same value to multiply variables
# site1 = site2 = 'Power Learn Project'
# print(site1)
# print(site2)

# ------------------------------------------------------------------------------

# # Understaning Data Types : int, float, str, bool, list, dict, and tuple

# # Numeric Data Type
# num1 = 5
# print(num1, 'is of type', type(num1))
# num2 = 2.0 
# print(num2, 'is of type', type(num2))
# num3 = 1 + 2j
# print(num3, 'is of type', type(num3))

# # List Data Type

# # enlose within breakets []
# languages = ['Swift', 'Java', 'Python']
# # access element at index 0
# print(languages[0])
# # access element at index 2
# print(languages[2])

# # Tuple
# product = ('Microsoft', 'Xbox', '499.99')
# print(product[0])
# print(product[1])

# # String Data TYpe
# name = 'Python'
# print(name)
# message = 'Python For Beginners'
# print(message)

# # Set Data Type
# student_id = {112,114,116,118,115}
# print(student_id)
# print(type(student_id))

# # Dictionary Data Type
# capital_city = {'Napal':'Kathemandu', 'Italy':'Rome', 'England':'London'}
# print(capital_city)
# # Access Dictionary values using keys
# capita_city = {'Napal':'Kathemandu', 'Italy':'Rome', 'England':'London'}
# print(capital_city['Napal'])
# print(capita_city['Kathemandu'])

# ----------------------------------------------------------------------------

# Types Conversion

num1 = 6
num2 = 9
print('This is output')

# Implicit Conversion (Converting Integer to Float)
integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
print("value:", new_number)
print("Data Type:", type(new_number))

# Explicit Conversion (Adding a string and integer Using)
num_string = '12'
num_integer = 23
print('Data Type of num_string before Type Casting',type(num_string))

num_string = int(num_string)
print("Data Type of num_sum after Type Casting:",type(num_string))

num_sum = num_integer + num_string
print("Sum:",num_sum)
print("Data Type of num_sum:", type(num_sum))

# -----------------------------------------------------------------

#  Basic Operations

sub = 10 - 5
print(sub)

# Python Assignment Operators

var = 5
print(var)

# Python Comparison Operators

a = 5
b = 2
print(a > b)

# Logical Operators

a = 5
b = 6
print((a > 2) and (b >= 6))

# -----------------------------------------------------------------------------

# Printing Output and Collecting User Input in Python

print('Good Norning!')
print('It is rainy today!')

# Syntax of print()
# print(object= seperator= end= file= flash=)
print('Good Morning,', end= '')
print('It is rainy today.')

# Print Python Variables and Literals
number = -10.6
name = "Power LP"
print(5)
print(number)
print(name)

# Print Concatenated Strings
print('PowerLP is' + ' awesome.')

# Python User Input
num = input('Enter a Number:')
print('You Entered:', num)
print('Data Type of num:', type(num))

# Weekly Code Challenge
# Exercise: User Input

# Ask the user for their name and store it in the variable "name"
name = input("What is your name? ")

# Ask the user for their age and store it in the variable "age"
age = input("How old are you? ")

# Ask the user for their location and store it in the variable "location"
location = input("Where do you live? ")

# Print out a personalized message using the user's name, age, and location
print("Hello {}, you are {} years old and live in {}.".format(name, age, location))
