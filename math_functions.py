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


abs_val = abs(-9)
print(abs_val)

max_number= max(1,5)
print(max_number)

max_str = max('a', 'b')
pritn(max_str)

min_number = min(1 ,2)
print(min_number)

numbers_sum = sum([1, 2])
print(numbers_sum)

rounded_number = round(3.45)

rounded_number_one_decimal = round(3.45, 1)
print(rounded_number_one_decimal)

cosine_val = math.cos(0)
print(cosine_val)

cosine_pi_val = math.cos(math.pi)
print(cosine_pi_val)

random_number_1 = random.randint(1, 10)
print(random_number_1)

random_number_2 = random.randrange(1, 10, 2)
print(random_number_2)


lst = ["he", "hi", "ho", "hello"]
random_choice = random.choice(lst)
print(random_choice)




