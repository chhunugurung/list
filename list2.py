fhand =open("romeo.txt","r")
my_words = []
for line in fhand:
    words=line.split()
    for word in words:
        if word not in my_words:
            my_words.append(word)
my_words.sort()
print(my_words)        