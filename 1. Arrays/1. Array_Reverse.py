# Day1 Challenge - Arrays

# Reversing the array in different methods
# Method 1 : Normal Way
from doctest import OutputChecker

def reverseArray(Arr, start, end):
    while start < end:
        Arr[start], Arr[end] = Arr[end], Arr[start]
        start += 1
        end -= 1
Arr = [1,2,3,4,5,6]
print("The Given Array is: ", Arr)
reverseArray(Arr, 0, 5)
print("The Reverse Array is: ", Arr)
print()

# Time Complexity : O(N)
# Output:
# The Given Array is:  [1, 2, 3, 4, 5, 6]
# The Reverse Array is:  [6, 5, 4, 3, 2, 1]

# Method 2 : Recursive Way
def reverseArray(Arr, start, end):
    if start >= end:
        return
    Arr[start], Arr[end] = Arr[end], Arr[start]
    reverseArray(Arr, start+1, end-1)
Arr = [1,2,3,4,5,6]
print("The Given Array is: ", Arr)
reverseArray(Arr, 0, 5)
print("The Reverse Array is: ", Arr)
print()
# Time Complexity : O(N)
# Output:
# The Given Array is:  [1, 2, 3, 4, 5, 6]
# The Reverse Array is:  [6, 5, 4, 3, 2, 1]


# Method 3 : Slicing Method
def reverseArray(X):
    print(X[::-1])

X = [1,2,3,4,5,6]
print("The Given Array is: ", X)
print("The Reverse Array is: " )
reverseArray(X)
# Output
# The Given Array is:  [1, 2, 3, 4, 5, 6]
# The Reverse Array is: 
# [6, 5, 4, 3, 2, 1]