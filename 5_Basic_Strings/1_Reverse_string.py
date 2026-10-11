# Given a string, the task is to reverse it. The string is represented by an array of characters s.
# Perform the reversal in place with O(1) extra memory.
# Note: no need to return anything, modify the given list.

# Example 1:
# Input : s = ["h", "e" ,"l" ,"l" ,"o"]
# Output : ["o", "l", "l", "e", "h"]

# Explanation :
# The given string is s = "hello" and after reversing it becomes s = "olleh".

def reverseString(s):
    left=0
    right=len(s)-1
    while left<right:
        s[left],s[right] = s[right], s[left]
        left+=1
        right-=1
        return s
s=['h', 'e', 'l', 'l', 'o']
print(f"Before Reverse : {s}")
print(f"After Reverse : {reverseString(s)}")

# Complexity:

# Time: O(n) — approximately half the characters are swapped.

# Extra space: O(1) — only two pointers and a temporary reference are needed.
