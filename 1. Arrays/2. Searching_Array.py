# Program to finding an element in an array based on user input

arr =[23, 44, 56, 78, 34, 22, 65, 67]
inp = input("Enter number for searching: ")
for i in range(1,len(arr),1):
    if int(inp) == arr[i] :
        print("The index of that number is: ", i)

# OP: Enter number : 78
# The index of that number is:  3

# Search an Element in an array - GFG Problem
# Given an integer array and another integer element. The task is to find if the given element is present in array or not.
# Input:
# n = 4
# arr[] = {1,2,3,4}
# x = 3
# Output: 2
# Explanation: There is one test case 
# with array as {1, 2, 3 4} and element 
# to be searched as 3.  Since 3 is 
# present at index 2, output is 2.

def search(self,arr, N, X):
        #Your code here
        if X in arr:
            return arr.index(X)
        return -1

# For Input: 
# 4
# 1 2 3 4
# 3

# Your Output: 
# 2

# Expected Output: 
# 2