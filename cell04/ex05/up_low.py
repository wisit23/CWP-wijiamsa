s = input("")
newword = ""
for i in s:
    if i.isupper():
        newword += i.lower()
    else:
        newword += i.upper()
print(newword)
        