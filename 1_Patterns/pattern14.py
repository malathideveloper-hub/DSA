n=5

for i in range(1,n+1):
    c="A"
    for j in range(1,i+1):
        print(c,end="")
        c=1+ord(c)
        c=chr(c)
    print()