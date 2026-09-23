import sys
if len(sys.argv) != 2:
    print("none")
else:
    a = False
    for i in range(len(sys.argv[1])):
        if sys.argv[1][i] == "z":
            print("z", end="")
            a = True
    if a == False:
        print("none")
    else:
        print()