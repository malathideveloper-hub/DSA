# You are given a integer n
# Return the largest digit present in the number 

# Input n=25
# Output : 5
# Explanation: The Largest digit in 25 is 5

def largest_num(n):
    large=0

    while n>0:
        last_digit=n%10
        if large < last_digit: large=last_digit
        n//=10
    return large

n=25
print(f"Largest number in {n} is {largest_num(n)}")

# Complexity

# Let d = number of digits.

# Time: O(d) — every digit is checked once.
# Space: O(1) — only a fixed number of variables are used.