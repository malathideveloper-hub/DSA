# You are given an integer n
# Return the interger formed by placing the digits of n in reverse order

# Example:

# input n=25
# output : 52

# Note: Reverse of 25 is 52

# Code:

def reverse(n):
    reverse_num=0
    while n>0:
        last_digit=n%10
        reverse_num=reverse_num*10+last_digit
        n=n//10
    return reverse_num


n=52
print(f"Reverse of {n} is {reverse(n)}")

# Logic:

# Get the last digit using n % 10.
# Add the digit to the reversed number:
#     reverse_num = reverse_num * 10 + last_digit
# Remove the last digit using n // 10.
# Repeat until n becomes 0.

# Time Complexity: O(d)
# → d = number of digits; each digit is processed once.

# Space Complexity: O(1)
# → Only a fixed number of variables are used.