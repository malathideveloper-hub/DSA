# Write a function to find the longest common prefix 
# string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input : str = ["flowers" , "flow" , "fly", "flight" ]
# Output : "fl"

# Explanation :
# All strings given in array contains common prefix "fl".

def longestCommonPrefix(s):
    s.sort()
    n=len(s)
    first=s[0]
    last=s[n-1]
    st=""
    if not s:
        return ""
    for i in range(0,min(len(first),len(last))):
        if first[i]!=last[i]:
            break
        else:
            st+=first[i]
    
    return st

s = ["flowers" , "flow" , "fly", "flight" ]
print(longestCommonPrefix(s))

# Time and space complexity

# Let n be the number of strings and m be the 
# maximum length of a string.

# Sorting: O(nlogn⋅m) in the typical character-comparison analysis.

# Comparing the first and last strings: O(m).

# Overall time complexity: O(nlogn⋅m).

# Auxiliary space: Depends on the sorting implementation; 
# Python's sorting may use up to O(n) auxiliary space. 
# Your prefix string can also use up to O(m) space.