# You are given an integer n
# Return the value of n! or n factorial

# Factorial of a number is the product of all positive integers less than or equal to that number

# Example 1

# input : n=4
# output : 24

# Explanation : 4! => 1 x 2 x 3 x 4 => 24


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i

    return fact

n=4

print(f"Factorial of {n} is {factorial(n)}")

# Complexity
# Time: O(n) → loop runs n times.
# Space: O(1) → only a fixed number of variables are used.
# ⭐ Important edge case

# Remember:

# 0! = 1

# Your code handles this correctly because:

# range(1, 0 + 1)

# runs zero times, so fact remains 1.