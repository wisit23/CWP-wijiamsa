import sys
print(f"parameters : {len(sys.argv)-1}")
for i in range(len(sys.argv)):
    if(i==0):
        continue
    print(f"{sys.argv[i]} : {len(sys.argv[i])}")
