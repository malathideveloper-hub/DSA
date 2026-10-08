# You are given an integer n. 
# You need to check if the number is prime or not. 
# Return true if it is a prime number, otherwise return false.

# A prime number is a number which has no divisors 
# except 1 and itself.

# Example 1:
# Input: n = 5

# Output: true

# Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

# def is_prime(n):
#     is_prime=True

#     for i in range(2,n):
#         if (n%i==0):
#             is_prime=False
#     return is_prime

# n=7
# print(f"{n} is a {"prime" if is_prime(n) else "Not a prime"}")

# *Brute-force* complexity:

# Time: O(n)
# Space: O(1)

# Optimised Approach
# if n has a divisor greater than √n, its paired divisor will be smaller than √n.

from math import sqrt
def is_prime(n):
    is_prime=True

    if n<=1:
        is_prime=False

    for i in range(2, int(sqrt(n)) + 1):
        if (n%i==0):
            is_prime=False
    return is_prime

n=7
print(f"{n} is a {"prime" if is_prime(n) else "Not a prime"}")

# No divisor → prime.

# Complexity
# Time: O(√n)
# Space: O(1)