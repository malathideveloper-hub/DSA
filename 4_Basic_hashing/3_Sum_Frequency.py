# Given an array of n integers, find the sum of the frequencies of the highest occurring number and lowest occurring number
# Example 2:
# Input: arr = [4, 4, 5, 5, 6]

# Output: 3

# Explanation: The highest frequency is 2 (elements 4 and 5), and the lowest frequency is 1 (element 6). Their sum is 2 + 1 = 3.


def sumHighestAndLowestFrequency(nums):
    d= dict()

    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
            
    # print(d)

    sum1=min(d.values())+max(d.values())
    # print(sum1)

    return sum1

arr=[4, 4, 5, 5, 6]
print(sumHighestAndLowestFrequency(arr))