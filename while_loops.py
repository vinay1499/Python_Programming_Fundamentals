#while loops

"""
* break()
* looping through a list


"""
num = input("Enter a number: ")

while not num.isdigit():
    num = input("Enter a number: ")


#or

while True:
    num = input("Enter a number: ")
    if num.isdigit():
        break

#list

# lst = [1,2,3,5,4,6,5,6,5]

# i = 0
# result = 0
# while i< len(lst):
#     result+=lst[i]
#     i+=1
# print(result)


#while - else

lst = [1,2,3,5,4,6,5,6,5]

i = 0

while i< len(lst):
    if lst[i] == -2:
        print("found it")
        break
    i+=1
else:
    print("Didn't found it")