n=5

for i in range(1,n+1):
    ch="A"
    for j in range(i,0,-1):
        pch=chr(ord(ch)+n-j)
        print(pch, end="")
    print()