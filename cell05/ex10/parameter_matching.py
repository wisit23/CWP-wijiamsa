import sys
a =True
if len(sys.argv)-1== 0 or len(sys.argv)-1 <1:
    print("none")
    a = False
while(a):
    s = input("What was the parameter? ")
    if sys.argv[1] == s:
        print("Good job!")
        break
    else:
        print("Nope, sorry...")