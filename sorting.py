#sorting

lst = [2,1,3,6,4,2,3,2,1]

lst.sort()
print(sorted(lst))
print(lst)

lst.sort(reverse=True)
print(lst)

print(sorted(lst, reverse=True))

lst1 = [[1,2], [3,4], [5,-6], [1,-2], [0, 0]]
lst1.sort(reverse=True)
print(lst1)

# if you want to sort it by using the second element, you have to use a keyword...

def sort_second_index(item):
    return item[1]
    
lst2 = [[1,2], [3,4], [5,-6], [1,-2], [0, 0]]
#lst2.sort(key = sort_second_index)
lst2.sort(reverse = True, key = sort_second_index)

print(lst2)


def sort_sum_index(item):
    return sum(item)

lst2.sort(reverse = True, key = sort_sum_index)

print(lst2)

new_lst = sorted(lst2, key = sort_second_index)
print(new_lst)
