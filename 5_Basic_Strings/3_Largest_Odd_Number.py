# Given a string s, representing a large integer, 
# the task is to return the largest-valued odd integer 
# (as a string) that is a substring of the given string s.

# The number returned should not have leading zero's. 
# But the given input string may have leading zero. 
# (If no odd number is found, then return empty string.)

# Example 1:
# Input : s = "5347"
# Output : "5347"

# Explanation :
# The odd numbers formed by given strings are --> 5, 3, 53, 347, 5347.
# So the largest among all the possible odd numbers for given string is 5347.

def largeOddNum(s):
    #find the end index
    n=len(s)
    end=None
    for i in range(n-1,-1,-1):
        if int(s[i])%2!=0:
            end=i
            break

    if end is None:
        return ""

    #find start index
    for i in range(0,n):
        if int(s[i])!=0:
            start = i
            break

    return s[start:end+1]

n="00012345642"
print(largeOddNum(n))

# Time Complexity (TC): O(n)
# First loop scans from right to left to find the last odd digit: worst case O(n).
# Second loop scans from left to right to find the first nonzero digit: worst case O(n).
# Total: O(n+n)=O(2n)=O(n).
# Here, n is the length of the string.

# Space Complexity (SC):Auxiliary space: O(1)