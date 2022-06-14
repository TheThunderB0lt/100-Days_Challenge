# Sort an array of 0s, 1s and 2s

# Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.
# Complexity Analysis: 
# Time Complexity: O(n). 
# Only one traversal of the array is needed.
# Space Complexity: O(1). 
# No extra space is required.
# Approach:
# Count the number of 0s, 1s and 2s in the given array. Then store all the 0s in the beginning followed by all the 1s then all the 2s.


def printArr(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

def sortArr(arr, n):
    c0 = 0
    c1 = 0
    c2 = 0

    for i in range(n):
        if arr[i] == 0:
            c0 += 1
        elif arr[i] == 1:
            c1 += 1
        elif arr[i] == 2:
            c2 += 1
        i = 0

    while(c0 > 0):
        arr[i] = 0
        i += 1
        c0 -= 1

    while(c1 > 0):
        arr[i] = 1
        i += 1
        c1 -= 1

    while(c2 > 0):
        arr[i] = 2
        i += 1
        c2 -= 1
    print ("Array after segregation :")
    printArr(arr, n)

#Driver code
arr = [0, 2, 1, 2, 1, 0, 0, 1, 2, 2, 1, 1 ,0, 2]
n = len(arr)
sortArr(arr, n)

# Output
# Array after segregation :
# 0 0 0 0 1 1 1 1 1 2 2 2 2 2 