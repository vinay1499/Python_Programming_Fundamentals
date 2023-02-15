'''
* A set is a unique collection of elements. no elements can be duplicated. 

* need to use a set() function for creating  set. and stored in curly bracdes {}.

* add() function for adding elements.
* remove() method removes the element given in the braces.

***  cannot add a list and a dictionary inside of a set.

* in operator

* union operator , union() or "|"

* intersection operator, intersection() or "&"

* difference .difference() or "-"

* symmetric difference  .symmetric_difference(y) or ^ , llr to the difference but results the elements that are not shared between the two sets 

* update(), add all ofthe elements in y to x. don't assign it to a variable.

* difference_update()

* symmetric_difference_update()

* subset

* superset -  a superset of an other set means that this set contains contains all of the elements potentiall more of another set. 

* proper subset

* proper superset

'''




from re import X


x = set()
x = {1,2,3,4,4,4,4,4}
print(x)
x.add(5)
x.remove(4)
print(x)

y = set()
y = {1,2,3,4,1,2,"hello", True,(1,2)}
print(y)
print(len(y))

contains =  1 in y
print(contains)

z = x.union(y)

print(z)

k = z|x
print(k)

f = x.intersection(y)
print(f)

s = f & x
print(s)

d = x.difference(y) # or y-x
print(d)

sd = x.symmetric_difference(y) #  or x ^ y
print(sd)

x.update(y)
print(x)
y.update(x)
print(y)

s= {1,4,5,3,2}

jk = s.difference_update(x)
print(jk)

super_Set = {1,2,3,4,5} # all the elemtents in the subset should be in the super set ;, x
sub_set = {1,2,3} # y

print(sub_set.issubset(super_Set))   # sub_set <= super_Set
print(sub_set <= super_Set)
print(sub_set >= super_Set)

#proper super set and proper subset

print(sub_set < super_Set)
print(sub_set > super_Set)
