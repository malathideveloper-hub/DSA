# You are given an integer n
# You need to return the number of odd digits present in the number
# The Number will have No Leading zeros except the number is 0 itself

# Example : 1

# Input n=25
# output : 1

# Note: The only odd digit is 25 is 5

n=2537
no_odd_digit=0

while n>0:
    last_digit = n%10
    if last_digit % 2 != 0:
        no_odd_digit+=1
    n=n//10

print(f"No.of odd digits is {no_odd_digit}")

# Complexity:
# d=> Number of digits
# TC = O(d)
# SC = O(1)

# Logic:

# Get the last digit using n % 10.
# Check whether the digit is odd using digit % 2 != 0.
# If odd → increment count.
# Remove the last digit using n // 10.
# Repeat until n becomes 0.

# Memory rule

# % 10 → get last digit
# // 10 → remove last digit

# This %10 + //10 combination is one of the most important basic-maths patterns in DSA, so make sure you remember it.