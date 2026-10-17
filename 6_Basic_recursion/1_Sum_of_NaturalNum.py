# Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.

# Example 1:
# Input : N = 4

# Output : 10

# Explanation : first four natural numbers are 1, 2, 3, 4.

# Sum is 1 + 2 + 3 + 4 => 10.


def NnumbersSum(n):
    #your code goes here
    if n==0:
        return 0
    return n+ NnumbersSum(n-1)

n=5

print(NnumbersSum(n))

# Complexity
# - Time: (O(n)) -> bcz of recursion
# - Auxiliary space: (O(n)), because the recursive calls use the call stack.