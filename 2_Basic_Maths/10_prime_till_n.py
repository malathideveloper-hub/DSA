# You are given an integer n. 
# You need to find out the number of prime numbers 
# in the range [1, n] (inclusive). 
# Return the number of prime numbers in the range.

# A prime number is a number 
# which has no divisors except, 1 and itself.

# Example 1:
# Input: n = 6

# Output: 3

# Explanation: Prime numbers in the range [1, 6] are 2, 3, 5.

def is_prime(n):
    is_prime=True

    for i in range(2,n):
        if (n%i==0):
            is_prime = False

    return is_prime

n=6
count=0
for i in range(2,n+1):
    if is_prime(i):
        count+=1

print(f"{count} numbers there in the range of {n}")

# Notes/Remember :

# 1 is not a prime number.

# def is_prime(n):
#     if n <= 1:
#         return False

# overall time complexity is approximately:

# Time: O(n²)

# Space:O(1)

#optimised approch:

# # sqrt(n)

# def is_prime(n):
#     is_prime=True

#     for i in range(2, int(sqrt(n))+1):
#         if (n%i==0):