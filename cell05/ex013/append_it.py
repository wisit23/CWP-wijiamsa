import sys
if len(sys.argv) == 1:
    print("none")
else:
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        if sys.argv[i].endswith("ism"):
            continue
        print(sys.argv[i] + "ism")