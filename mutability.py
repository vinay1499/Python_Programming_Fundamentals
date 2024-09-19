'''
mutability - changeable. 
immutable - not changeable.

Immutable: In python, an immutable object is one that cannot be modified once created. 
The following are the examples of immutable data types:
int, float, str, bool, tuple

The following are the example of mutable data types:
list, set, dict

'''


x = 1
y = x
x += 1

print(x, y)


a = []
b = a
a.append(2)

print(a)
print(b)


# is keyword

print(x == y)
print(x is y)

print(a == b)
print(a is b)

# id is kind of a memory address location of objects in python.

s = 1
t = s

print(id(s), id(t))
print(id(x), id(y))


# more examples

'''
Mutable objects can be changed after they are created. 
This means that you can modify the object in place without 
needing to create a new object. 

Common mutable data types in Python include:
- Lists
- Dictionaries
- Sets

'''

# list

'''

Description: A list is an ordered collection of items 
that can be changed (mutated) after its creation.

'''

my_list = [1, 2, 3]
my_list.append(4)  # Modifying the list by adding an element
my_list[0] = 100   # Modifying an element at a specific index
print(my_list)     # Output: [100, 2, 3, 4]


# dictionary

'''
Description: A dictionary stores key-value pairs 
and allows modifying, adding, or removing elements.
'''

my_dict = {'name': 'Sai', 'age': 25}
my_dict['age'] = 26  # Modifying the value of an existing key
my_dict['city'] = 'Clemson'  # Adding a new key-value pair
print(my_dict)  # Output: {'name': 'Sai', 'age': 26, 'city': 'Clemson'}


# Set

'''

Description: A set is an unordered collection of unique items. 
You can add or remove items.

'''

my_set = {1, 2, 3}
my_set.add(4)    # Adding an element
my_set.remove(2)  # Removing an element
print(my_set)    # Output: {1, 3, 4}


'''

Immutable Objects:

Immutable objects cannot be changed after they are created. 
If you attempt to modify an immutable object, you will actually 
create a new object rather than modifying the existing one. 

Common immutable data types in Python include:

- Integers
- Floats
- Strings
- Tuples
- Frozen Sets

'''


# integers

'''

Description: Integers are whole numbers, and they cannot be changed once assigned.

'''

x = 10
y = x + 5  # x remains unchanged
print(x)   # Output: 10
print(y)   # Output: 15


# float

'''

Description: Floats are numbers with decimal points. They are also immutable.

'''

a = 1.5
b = a + 2.5  # a remains unchanged
print(a)     # Output: 1.5
print(b)     # Output: 4.0

  
# String

'''

Description: Strings are sequences of characters, and they cannot be changed after they are created.

'''

my_string = "Hello"
new_string = my_string + " World"  # Creates a new string
print(my_string)   # Output: Hello
print(new_string)  # Output: Hello World



# Tuple

'''

Description: Tuples are ordered collections like lists, but they are immutable.

'''

my_tuple = (1, 2, 3)
# my_tuple[0] = 100  # This will raise an error: TypeError: 'tuple' object does not support item assignment
print(my_tuple)    # Output: (1, 2, 3)


# frozen set

'''

Description: A frozen set is an immutable version of a set. 
Once created, elements cannot be added or removed.

'''

my_frozenset = frozenset([1, 2, 3])
# my_frozenset.add(4)  # This will raise an error: AttributeError: 'frozenset' object has no attribute 'add'
print(my_frozenset)    # Output: frozenset({1, 2, 3})
