# Pattern - 15

# A B C D E
# A B C D
# A B C
# A B
# A

n = 5

for i in range(n,0,-1): #5 4 3 2 1
    ch='A'
    for j in range(i):
        print(ch, end=" ")
        num=ord(ch)+1
        ch=chr(num)
    print()