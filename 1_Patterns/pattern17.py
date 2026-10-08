n = 5

for i in range(1, n + 1):

    # spaces
    for j in range(n - i):
        print(" ", end="")

    # characters
    ch = "A"

    for k in range(2 * i - 1):
        print(ch, end="")

        if k < i - 1:
            ch = chr(ord(ch) + 1)
        else:
            ch = chr(ord(ch) - 1)

    print()