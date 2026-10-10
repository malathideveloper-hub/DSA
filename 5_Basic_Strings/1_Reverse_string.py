# Given a string, the task is to reverse it. The string is represented by an array of characters s.
# Perform the reversal in place with O(1) extra memory.
# Note: no need to return anything, modify the given list.

# Example 1:
# Input : s = ["h", "e" ,"l" ,"l" ,"o"]
# Output : ["o", "l", "l", "e", "h"]

# Explanation :
# The given string is s = "hello" and after reversing it becomes s = "olleh".

def reverseString(s):
    s=list(s)
    print(s)
    left=0
    right=len(s)-1

    while left<right:
        temp=s[left]
        s[left]=s[right]
        s[right]=temp
        left+=1
        right-1
    print(s)
s="hello"
reverseString(s)
# print(s)


