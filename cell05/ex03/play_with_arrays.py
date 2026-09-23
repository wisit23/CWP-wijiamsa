array = [2, 8, 9, 48, 8, 22, -12, 2]
array2 = []
newarray = []
for i in range(len(array)):
    duplicate = False
    for j in range(len(array2)):
        if array[i] == array2[j]:
            duplicate = True
            break
    if duplicate == False:
        array2.append(array[i])
print(array2)
for i in range(len(array2)):
    if(array2[i] > 5):
        newarray.append(array2[i]+2)
print(newarray)