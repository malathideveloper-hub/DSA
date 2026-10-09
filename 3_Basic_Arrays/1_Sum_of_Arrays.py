# Given an array arr of size n, the task is to find the sum of all the elements in the array.

# Example 1:
# Input: n=5, arr = [1,2,3,4,5]

# Output: 15

# Explanation: Sum of all the elements is 1+2+3+4+5 = 15

def sum_of_array(arr, n):
    sum1=0
    for i in range(0,n):
        sum1+=arr[i]
    return sum1

n=5
arr = [1,2,3,4,5]

print(f"sum of arrays of {arr} is {sum_of_array(arr,n)}")