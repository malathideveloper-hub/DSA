# Given an array of n elements. The task is to return the count of the number of odd numbers in the array.
# Example 1:
# Input: n=5, array = [1,2,3,4,5]
# Output: 3
# Explanation: The three odd elements are (1,3,5).

class Solution:
    def countOdd(self, arr, n):
        count=0
        for i in range(0,n):
            if arr[i]%2==1:
                count+=1
        return count
ob=Solution()
n=5
array = [1,2,3,4,5]
print(f"Number of Odd elements in the array {array} is {ob.countOdd(array,n)}")