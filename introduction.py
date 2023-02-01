#Introduction

#   1- introduction
#       Python is a general purpose programming and scripting language. Python is known for being easy to learn and providing simple, 
#       yet powerful syntax. Python is mainly used for :- Machine learning, Artificial Intelligence, Data Science, Finance Applications,
#       web development, scripting, and task automation. 

#   2 - Datatypes
a = 3

print(f"type of {a}", type(a))

b = None
print(f"type of {b}", type(b))

c= True
print(f"type of {c}", type(c))

d = "letter"
print(f"type of {d}", type(d))


#   comments

#single line comment using a pound sign

'''
tripple quoted string 
multi line comment
hello 


'''

'''
you should use comment only if it is adding value to your comment...
'''


#   3 - variables and printing

# A variable can be thought of as a container that stores a value. As a programmer you can create your own 
#  variables that store different data types.

# in python variable names must:
# not start with a number, not contain any special characters other than  underscores(_), not contain any spaces.

hello_world = "this variable holds a string."

print("hello",5,True)
#prints in a new line because "\n" and it is invincible
print("Tim")

print("tim\n","Sai")

print("tim","Sai", end=" | ")
print("vinay")


#   5 - Console Input

#for most software to be useful, it needs to be able to be take in some sort of user input. 
# The input function is built directly into python as means to gather information from the command line.
# An important note is that it always returns a str object which will need to be converted to an int (for example) if you expect
#  the user input to be an integer

user_name = input("What is your name? ")
print("Hello", user_name , "!")
print(f"Hello {user_name} !")
# the below line won't work because for the input we shouldn't use ",". we should use concatenation "+"
#pwd = input("Hey", user_name, "Enter your password: ")
pwd = input("Hey " + user_name + " Enter your password: ")
agee = input("Hey "+user_name+ " Enter your age: ")

print("Hey "+ user_name +" your age is "+ agee + ".")




#================= Practice ===========================================================