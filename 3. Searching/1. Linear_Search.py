# Linear Search by user input

# Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].

# Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}  x = 110;
# Output : 6
# Element x is present at index 6

# Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}  x = 175;
# Output : -1
# Element x is not present in arr[].

from array import *

def linearSearch(arr, n, key):
     #Searching
    for i  in range(0, n):
        if (arr[i] == key):
            return i
    return -1

##Driver Code
arr = array('i', [])
n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the elements: "))
    arr.append(x) # array elements adding
print(arr)

key = int(input("Enter element to search: "))

##Function Call
result = linearSearch(arr, n, key)
if (result == -1):
    print("Element not found in arr[] ")
else:
    print("Element found at index: ", result)

# OUTPUT:
# Enter the length of the array: 5
# Enter the elements: 12
# Enter the elements: 13
# Enter the elements: 14
# Enter the elements: 15
# Enter the elements: 16
# array('i', [12, 13, 14, 15, 16])
# Enter element to search: 13
# Element found at index:  1

# Enter element to search: 17     
# Element not found in arr[] 