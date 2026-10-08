# You are given an integer N

# You need to check whether it is an armstrong number or not
# Return True if it is an armstrong number , otherwise retrn False

# An Armstrong number is a number which is equal to the sum of the digits of a number
# raised to the power of the number of digits

# Example:

# Input: n=153
# Output : True

# Explanation:
# Number of digits => 3
# => 1^3+5^3+3^3
# => 1+125+27
# => 153

# Therefore, it is an Armstrong number
from math import log10, pow

def count_digits(n):
    count=0
    while (n>0):
        last_digit=n%10
        count+=1
        n//=10
    return count
def armstrong(n):
    #find the length of a n value
    # count=log10(n)+1  #shortcut to find the count of digits
    count=count_digits(n) #=> O(d)
    n1=n
    num=0
    while n>0:
        last_digit=n%10
        # num+=pow(last_digit,count)
        # Python's math.pow() always returns a float.
        num+=last_digit**count # return int type value
        n//=10
    print(n1,num)
    return num == n1


# Complexity:

# count_digits() → O(d)
# Armstrong calculation → O(d)
# Overall → O(d)
# Space → O(1)

# n=153
# print(f"{n} is a {"Armstrong number" if armstrong(n) else "not a Armstrong number" } ")