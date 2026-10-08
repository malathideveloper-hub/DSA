n=5

for i in range(1,n+1):
    start=0 if i%2 == 0 else 1
    for j in range(i):
        print(start, end=" ")
        start= 1-start
    print()