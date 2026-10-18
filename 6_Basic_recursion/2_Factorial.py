# Given an integer n, return the factorial of n.

# Factorial of a non-negative integer, is the multiplication of all integers smaller than or equal to n (use 64-bits to return answer).

# Example 1:
# Input : n = 3

# Output : 6

# Explanation : Factorial = 1 * 2 * 3 => 6

def factorial(n):
    if n==0:
        return 1
    
    return n*factorial(n-1)
    
print(factorial(5))

# Complexity
# - Time complexity: \(O(n)\)
# - Auxiliary space complexity: \(O(n)\), due to the recursion call stack.