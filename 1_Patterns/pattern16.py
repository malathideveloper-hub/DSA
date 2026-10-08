n=5

ch="A"
for i in range(1,n+1):
    for j in range(i):
        print(ch, end=" ")
    print()
    num=ord(ch)+1
    ch=chr(num)