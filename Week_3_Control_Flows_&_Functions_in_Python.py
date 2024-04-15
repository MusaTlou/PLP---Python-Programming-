# # #  Coditional Statements (if.if..else and if..elif)

# # If Statement
# num = 20
# if num >= 20:
#    print("The number is: ", num)

# # if..else Satement
# bill = 2500

# discount = 100

# if bill > 2000:
#    print("Bill is greater than 2000!")
#    bill = bill - discount 
# else:
#   print("Bill is less than 2000!")

# print("Final bill: " + str(bill))

# # if..elif Satement
# # syntax 
# # if condition 1: 
# #  Block of code 1
# # else condition: 
# #  Block of code 2
# # elif condition: 
# #  Block of code 3

# # Write an if/else/elif statement for a college with a grading system as shown below:

# grade = 83

# if grade >= 90:
#    print("A")
# elif grade >= 80:
#    print("B")
# elif grade >= 70:
#    print("C")
# elif grade >= 60:
#    print("D") 
# else:
#    print("F")


# # Loops (for loops & while loop)
# # for loop sytax:
# # for <temporary variable> in <collection>:
# #  <action>
# names = ["Paul", "Skinny", "Ahmed", "Saruni"]

# for name in names:
#    print("Names:",name)

# # For Loops: Using Range
# welcome_message = "Welcome to PLP"

# for i in range(5):
#    print(welcome_message)


# # While Loops
# # While loop structure or syntax
# #  while <conditional statement>:
# #       <action>

# count = 0
# while count <= 2:
#    print(count)
#    count += 1

# # Loop controls: Break and continue
# # Using for loop
# colors = ["blue","green","white","yellow","brown"]
# color_i_want = "white"

# for color in colors:
#    if color == color_i_want:
#       print("They have the color i want!", color)
#       break
#    print(color)

# # Using while loop
# colors = ["blue","green","white","yellow","brown"]
# color_i_want = "white"

# length = len(colors)
# count = 0

# while count < length:
#    print(colors[count])

#    if colors[count] == color_i_want:
#        print("They have the color i want!", color_i_want)
#        break
#    count += 1

# # Python continue Stetement
# ages =[13, 24, 17, 36]

# for age in ages:
#    if age < 21:
#       continue
#    print(age)

# # Nested Loops
# groups = [["Paul", "Skinny"], ["Ahmed", "Gregory"]]

# for group in groups:
#    for name in group:
#       print(name)

# # List Comprehension
# nums = [4, -11, 69, 53, -65]
# doubled = []
# for num in nums: 
#   doubled.append(num * 2)

# print(doubled)

# # -------------------------------------------------------------------------

# # Python Functions

# # Function without parameters
# # def <function_name>:
# # <task to complete>

# # Functions with parameters
# # def <function_name(a, b)>:
# # <task to complete>

# #  creating a function and calling it
# def add_nums():
#    print(2 + 13)

#    add_nums()

# # Function Arguments/Parameters
# def add_nums(a, b):
#    answer = a + b
#    return answer
# # assign function call to a variation called total
# total = add_nums(2, 13)
# print("Total : ", total)

# # Arbitrary Arguments, *args

# # # If the number of arguments is unknown, add a * before the parameter name:
# def add_nums(*nums):
#    sum = 0
#    for num in nums:
#       sum += num
#       return sum
#    print("Total: ", add_nums(2, 5, 6, 7, 8, 13))

# # Arbitrary Keywoord Arguments,**kwargs
# # If the number of kwargs is unknown, add a ** before the parameter name:
# def add_ages(**ages):
#    sum = 0
#    for k, v in ages.items():
#       sum += v
#       return sum
#    print("Total: ", add_ages(mutemi=23, skinny=22, ahmed=21))

# #------------------------------------------------------------------------------------------

# # Functions and Variables Scopes

# # Local Scope
# def add_nums(a, b):
#    #  local variable declared inside a function
#    answer = a + b
#    return answer
# # calling our function inside print statement
# print(add_nums(2, 13))

# # Enclosing Scope
# def add_nums(a, b):
#    # enclosed variable declared inside a function
#    answer = a + b
#    def double_it():
#       double = answer * 2
#       print(double)
#    double_it() 
#    return answer
# # calling our function inside print statement
# print(add_nums(2, 13)) 

# # Global Scope
# global_var = 13

# def add_nums(az, bo):
#    # enclosed scope variable declared inside a function
#    total = az + bo
#    print("Global_var in inner function: ", global_var)
#    def double_it():
#       # Local variable
#       double = total * 2
#       print("Global_var in inner function: ", global_var)
#       # if you want to print out double uncomment line below
#       # print("Double: ", double)
#    double_it()
#    return total
   
# add_nums(13,5)

# ------------------------------------------------------------------------

# Python Lambda Functions

# Syntax:
# lambda arguments(s): expression
# or
# lambda <funcyion_paraemter>: <return_value>

snack = lambda : print("Njugu")

# calling the lambda
snack()

#  A lambda function with arguments

# This a Function called num_square
def num_square(num):
    return num ** 2 
# calliing out num_square function with argument set to num=8
print("Square of num is: ", num_square(8))

# Rewriting the abouve num_square function using Lambda Function knowledge
num_square = lambda num: num ** 2
# callijg the lambda inside print()
print("Square of num is: ", num_square(8))


# A normal python function to determin a Palindrome of a given string
def isPalindrome(string):
    if (string == string[::-1]):
        return "A Palindrome."
    else:
        return "Not a Palindrome."
    
# Enter input string
string = input("Enter string:")

# call the function and pass input from the user - string variable
print(isPalindrome(string))

# Rewrite the above function uing Lambda Function:
isPalindrome = lambda string : "Palindrome" if string == string[::-1] else "Not Palindrome."
string = input("Enter string:")

# calling our lambda and passing string argument
print(isPalindrome(string))

