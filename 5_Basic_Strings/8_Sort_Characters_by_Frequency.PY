# You are given a string s. Return the array of unique 
# characters, sorted by highest to lowest occurring characters.
# If two or more characters have same frequency then 
# arrange them in alphabetic order.

# Example 1:
# Input : s = "tree"

# Output : ['e', 'r', 't' ]

# Explanation :
# The occurrences of each character are as shown below :
# e --> 2
# r --> 1
# t --> 1.
# The r and t have same occurrences , so we arrange them 
# by alphabetic order.

def frequencySort(s):
    # 1) find the frequency
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print("frequency : ",freq)
    #You need to sort using two rules:
    # Frequency — highest to lowest.
    # Alphabetical order — A to Z when frequencies are equal.

s = "tree"
print(frequencySort(s))