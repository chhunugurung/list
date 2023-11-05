fhand = open("mbox file","r")
count = 0
for line in fhand:
    if line.startswith("From") and not line.startswith("From:"):
        word = line.split()
        if len(word) > 1:
            sender = word[1]
            print(sender)
            count = count + 1
fhand.close()
print("Total {count} line were printed")    