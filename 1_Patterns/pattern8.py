n = 5

for i in range(1, n + 1):

    # spaces
    for j in range(i - 1):
        print(" ", end="")

    # stars
    for k in range(2 * (n - i) + 1):
        print("*", end="")

    print()