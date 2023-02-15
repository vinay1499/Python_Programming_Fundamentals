# math

import math
import random


'''

built in math functions:
abs()
max() -  gives the max value inside of an iterable list, tuple ..or the arguments you pass.
min()
sum()
round()

math module

random module
randint
randrange


'''


# x = abs(-9)
# x = max(1,5)
# x = max('a', 'b')
# x = min(1 ,2)
# x = sum([1, 2])
# x = round(3.45)
#x = round(3.45, 1)

# x = math.cos(0)

x = math.cos(math.pi)

print(x)

# random_number = random.randint(1, 10)

random_number = random.randrange(1, 10, 2)

print(random_number)

lst = ["he", "hi", "ho", "hello"]

random_choice = random.choice(lst)

print(random_choice)




