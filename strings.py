#strings
"""
len(), count(), find() - gives the index of the character , upper(), lower(), capitalize() - capitalizes the first letter in the string.
isdigit() - only returns true if the value is int, .split(), replace(), fstrings, *n, multi line string, escape character \, " ".join(). 

"""

s = "hello"
print(len(s))

count = s.count("l")
print(count)

find = s.find("o")

print(find)

upper = s.upper()
print(upper)

answer = input("Enter your name: ")

if answer.lower() == "tim":
    print("Welcome")
else:
    print("Try again!!")


#
capitalizing = "saivinay"

print(capitalizing.capitalize())

contains = "h" in capitalizing
print(contains)

is_digit = "19" #won't return true for "19h", "19.4",.....
print(is_digit.isdigit())


sentence = "Hello my name is vinay"

words = sentence.split()

print(words)

sentence_2 = "Hello,my,name,is,vinay"
words_2 = sentence_2.split(",")
print(words_2)



sentence_1 = "Hello,my-name.is.vinay"



for i in sentence_1:
    if i in """.,- """:
        sentence_1 = sentence_1.replace(i," ")

words_1 = sentence_1.split(" ")

print(words_1)


sentence_replace = "hello, my, name, is ,,,,vinay"

sentence_replace = sentence_replace.replace(",","|")

print(sentence_replace)

enter_name = input("Enter your name: ")
print("Hello", enter_name , "!!")
print("Hello", enter_name + "!!")
print(f"Hello {enter_name} !!")

print(enter_name *5)

multi_line_string = """ hello my name 
is sai vinay 
Nandigam

"""

#escape characters

print(f"hello \'{enter_name}")


lst = ["s","a","i"]

print_lst = " ".join(lst)

print(print_lst)