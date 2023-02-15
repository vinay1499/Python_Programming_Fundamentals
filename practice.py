sentence_1 = "Hello,my-name.is.vinay"
for i in sentence_1:
    if i in """.,- """:
        sentence_1 = sentence_1.replace(i," ")

# words_1 = sentence_1.split(" ")

print(sentence_1)