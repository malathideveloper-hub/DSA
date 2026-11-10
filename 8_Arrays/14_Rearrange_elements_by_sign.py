# Given an integer array nums of even length consisting of an equal number of positive and negative integers.Return the answer array in such a way that the given conditions are met:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Example 1:
# Input : nums = [2, 4, 5, -1, -3, -4]

# Output : [2, -1, 4, -3, 5, -4]

# Explanation:

# The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4 maintain their relative positions

# My brute force approach
nums=[3, -5, 8, -2, 9, -7]

ptive=[]
ntive=[]

for i in nums:
    if i>0:
        ptive.append(i)
    else:
        ntive.append(i)
        
# print(ptive)
# print(ntive)

n=len(nums)//2
# print(n)
res=[]
for i in range(n):
    res.append(ptive[i])
    res.append(ntive[i])
    
print(res)

#My Optimised Approch

nums = [2, 4, 5, -1, -3, -4]

res = [None] * len(nums)

p = 0
n = 1

for i in nums:
    if i > 0:
        # Place positive number
        res[p]=i
        # Increment p by 2
        p+=2

    else:
        # Place negative number
        res[n]=i
        # Increment n by 2
        n+=2

print(res)