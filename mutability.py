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
x+=1

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