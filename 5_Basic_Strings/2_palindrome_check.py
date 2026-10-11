# You are given a string s. Return true if the string is palindrome, otherwise false.
# A string is called palindrome if it reads the same forward and backward.
# Example 1:
# Input : s = "hannah"
# Output : true

# Explanation :
# The given string when read backward is -> "hannah", which is same as when read forward.
# Hence answer is true.

# Ans :  Two pointer approch

def palindromeCheck(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

s = "hannah"
print(f" Given string is {'palindrome' if palindromeCheck(list(s)) else 'Not Palindrome'}")
# notes

# Approach: Two pointers

# Time complexity: O(n) — at most half the string is checked, which simplifies to O(n).

# Auxiliary space: O(1) — only two pointers are used.

# Key idea: Compare characters from opposite ends and move inward.