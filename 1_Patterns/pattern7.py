n=5

for i in range(1,n+1):
    #print space
    for j in range(1,(n-i)+1):
        print(" ",end="")
    #print star
    for k in range(1,(i*2-1)+1):
        print("*", end="")
    print(" ")