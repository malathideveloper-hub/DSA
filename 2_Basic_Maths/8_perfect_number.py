# Re - Do
# You are given an integer n. You need to check if the number is a perfect number or not. Return true if it is a perfect number, otherwise, return false.

# A perfect number is a number whose proper divisors (excluding the number itself) add up to the number itself.

# Example 1:
# Input: n = 6

# Output: true

# Explanation: Proper divisors of 6 are 1, 2, 3.

# 1 + 2 + 3 = 6.

# Solution - 1 : Bruteforce

# def is_perfect1(n):
#     sum=0
#     for i in range(1,n):
#         if (n%i == 0):
#             sum+=i
#     print(n,sum)
#     return n == sum
# n=6
# print(f"{n} is a {"perfect number" if is_perfect1(n) else "Not a perfect number"}")

# Solution -2 - Optimised
from math import sqrt
def is_perfect2(n):
    # till sqrt(n)
    sum=1
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            pair=n//i
            sum+=i
            if pair!=i:
                sum+=pair
    print(sum)
    return n==sum

n=6
print(f"{n} is a {"perfect number" if is_perfect2(n) else "Not a perfect number"}")