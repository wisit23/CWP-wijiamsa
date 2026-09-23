import sys
if len(sys.argv)-1 >2:
    print("none")
elif len(sys.argv)-1 == 0 :
    print("none")
else:
    print(sys.argv[2].count(sys.argv[1]))
