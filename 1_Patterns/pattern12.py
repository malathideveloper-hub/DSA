n=5

#first pyramid

for i in range(1,n+1):
    #print numbers
    for j in range(1,i+1):
        print(j,end="")

    #space
    for _ in range(2*(n-i)):
        print(" ",end="")

    #print revert
    for l in range(i,0,-1):
        print(l,end="")

    print()