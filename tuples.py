#tuples

#it's not two pull its tah pull 

"""
A tuple is similar to a list that it stores a collection of elements. Like lists you can access individual elements in a 
tuple using their indicies, but you cannot modify or change these elements  

* cannont directly modify elements like x[0] = 5
* count()
* index()
* contains 2 in x
* (1,2,(2,3), True,"sai", [])
* combine x+y
* immutable
* len()
"""

x = (1,2,3,4)
print(x[2])
print(x[-1])

count = x.count(2)
print(count)

index = x.index(3)
print(index)

contains = 2 in x
print(contains)

y = ("sai", 3,7)

combine = x+y
print(combine)

#multiply = (2)*4
multiply = [2]*4
print(multiply)

a= 1,2,3,4
print(a) #when you print you can see a tuple
