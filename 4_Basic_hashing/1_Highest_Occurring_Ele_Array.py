# Given an array nums of n integers, 
# find the most frequent element in it i.e., 
# the element that occurs the maximum number 
# of times. If there are multiple elements 
# that appear a maximum number of times, find the smallest of them.
# Example 1:
# Input: nums = [1, 2, 2, 3, 3, 3]

# Output: 3

# Explanation: The number 3 appears the most (3 times). It is the most frequent element.

nums = [1, 2, 2, 2, 3, 3, 3]

f=dict()

for i in nums:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)

l=list(f.keys())

print(l)

m=max(l)

print(m)

print(f[m])

# partial solution done - now need to think .........