firstnum = int(input("Enter the first number: "))
secondnum = int(input("Enter the second number: "))
result = firstnum * secondnum
print(f"{firstnum} x {secondnum} = {result}")
if(result > 0):
    print("The result is positive.")
elif(result < 0):
    print("The result is negative.")
else:
    print("The result is positive and negative.")