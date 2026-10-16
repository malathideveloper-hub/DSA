# Given an array of n integers, 
# find the second most frequent element in it.

# If there are multiple elements 
# that appear second most frequent times, find the smallest of them.

# If second most frequent element does not exist return -1.

# Example 1:
# Input: arr = [1, 2, 2, 3, 3, 3]
# Output: 2

# Explanation:

# The number 2 appears the second most (2 times) 
# and number 3 appears the most(3 times). 

def secondMostFrequentElement(nums):
    d=dict()

    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    freq=0
    sec_freq=0
    ans=-1
    for key,value in d.items():
        if freq<value: # will get the max frequency
            freq=value

    # now i hv the freq holds the max frequency
    # lets find out the second most frequency

    for k,v in d.items():
        if freq>v:
            if sec_freq<v:
                sec_freq=v
                ans=k
            elif sec_freq == v:
                if ans>k:
                    ans=k
    return ans

# arr = [1, 2, 2, 3, 3, 3]
# arr = [4, 4, 5, 5, 6, 7]
arr = [1, 1, 2, 2, 3, 3]
print(secondMostFrequentElement(arr))


# ### Time Complexity
# - Building frequency dictionary: O(n)
# - Finding maximum frequency: O(k)
# - Finding second-highest frequency: O(k)

# **Overall Time Complexity:** O(n) average, because k ≤ n.

# ### Space Complexity
# - Dictionary stores k distinct elements.

# **Space Complexity:** O(k), worst case O(n).

# Where:
# - n = total number of elements
# - k = number of distinct elements