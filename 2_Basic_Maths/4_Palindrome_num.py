# You are given an integer n
# You need to check whether the number is a palindrome or not
# Return 'true' if it's a palindrome number, otherwise retrun false

# A palindrome number is a number which reads the same
# both left to right and right to left

# Example:

# input n=121
# output : True

# Note: when read from left to right 121
#       when read from right to left 121

# Code:

def is_palindrome(n):
    n1=n
    reverse_digit=0
    while n>0:
        last_digit=n%10
        reverse_digit=reverse_digit*10+last_digit
        n=n//10

    return reverse_digit == n1

n=121
print(f"Given number {n} is {'palindrome' if is_palindrome(n) else 'Not Palindrome'}")

# Complexity

# Let d = number of digits.

# Time Complexity: O(d) — each digit is processed once.
# Space Complexity: O(1) — only a fixed number of variables are used.
# 🔑 Memory Rule

# Store original → reverse the number → compare original and reversed number.