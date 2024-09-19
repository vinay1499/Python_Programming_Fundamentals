'''
Comprehension - initializing a data type,

Multiple Assignment - 

Unpacking - takin a tuple or list and unpacking it.

docstrings - a docstring is a multi line string or comment. It decribes or documents what a function does.

help() function - take a function or class and helps to read the docstring.

'''

# list comprehension

lst = []

for i in range(1,11):
    lst.append(i)
print(lst)

# better way

new_lst = [i for i in range(1, 11)]

print(new_lst)

multiply_by2_lst = [i * 2 for i in range(1, 11)]
print(multiply_by2_lst)

condition_lst = [i / 2 for i in range(1, 11) if i % 2 == 0]
print(condition_lst) 

nested_list = [i * j for i in range(1, 11) for j in range(5)]
print(nested_list)

dictionary_list = {i : j for i in range(1, 11) for j in range(5)}
print(dictionary_list)


# multiple assignments

x = y = 1

print(x, y)


# unpacking

a, b = (1, 2)
print(a, b)

