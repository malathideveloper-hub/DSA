# Given two strings s and goal, 
# return true if and only if s can become goal after some 
# number of shifts on s.
# A shift on s consists of moving the leftmost character 
# of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after 
# one shift.

# Example 1:
# Input : s = "abcde" , goal = "cdeab"

# Output : true

# Explanation :

# After performing 2 shifts we can achieve the goal string from string s.
# After first shift the string s is => bcdea
# After second shift the string s is => cdeab.

def rotateString(s, goal):
        if len(s) != len(goal):
            return False
        s1=s+s
        return goal in s1

s = "abcde"
goal = "cdeab"
print(rotateString(s,goal))

# 1. Time Complexity (TC): O(n)

# Breakdown:

# len(s) != len(goal) → O(1), because Python strings store their lengths.
# s1 = s + s → O(n), because a new string of length 2n is created.
# goal in s1 → typically O(n) for this substring-search operation in this approach.
# Therefore:O(1)+O(n)+O(n)=O(n)

# 2. Space Complexity (SC): O(n)

# s1 = s + s creates a new string containing 2n characters.
# Its space grows proportionally with the input length.
# Therefore: O(n)
