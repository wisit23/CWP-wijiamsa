array = [2, 8, 9, 48, 8, 22, -12, 2]
newarray = []
for i in range(len(array)):
    if(array[i] > 5):
        newarray.append(array[i]+2)
print(newarray)