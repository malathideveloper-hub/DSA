# You are given two integers n1 and n2. 
# You need find the Greatest Common Divisor (GCD) 
# of the two given numbers. Return the GCD of the two numbers.

# The Greatest Common Divisor (GCD) of 
# two integers is the largest positive 
# integer that divides both of the integers.

# Example 1:
# Input: n1 = 4, n2 = 6

# Output: 2

# Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6

# Greatest Common divisor = 2.

# Brute force soution

def gcd_bruteforce(n1,n2):
    largest=1
    for i in range(1,min(n1,n2)+1):
        if (n1%i==0) and (n2%i==0):
            largest=i
    return largest

n1=20
n2=40
print(f" GCD of the {n1} and {n2} is {gcd_bruteforce(n1,n2)}")

# Time: O(min(n1, n2))
# Space: O(1)

