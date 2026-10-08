# You are given an integer n
# You need to return the number of digits in the number
# The number will have no leading zeros,
# except when the number is zero itself

# Eg:
# input :
# n=5678
# output:
# 4
# Note: there is 4 digits in n

#Solution 1:

# n=5467
# s=str(n)
# print(f"Number of digits in {n} is {len(s)}")

# solution 2
# n=2345

# count=0
# while n>0:
#     n=n//10
#     count+=1

# print(count)

#solution 3
# n=1234
# from math import log10
# print(round((log10(n)+1)))


# whats the Time and space complexity ?

# d=> number of digits
# TC = O(d)
# SC = O(1)