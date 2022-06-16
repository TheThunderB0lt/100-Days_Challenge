# Bubble Sort
# Simplest sorting algorithm. Iterates over the list, in each iteration it compares elements in pairs and keeps 
# swapping them such that the larger element is moved towards the end of the list.

#It has a time complexity of O(n2) in the average and worst cases scenarios and O(n) in the best-case scenario.
# Non recursive
# Stable
# In place
# O(n²)

# from array import *

def bubbleSort(arr):

    for i in range(len(arr)-1, 0, -1):

        for j in range(i):

             if arr[j] > arr[j+1]: # Checking neghbours

                arr[j], arr[j+1] = arr[j+1], arr[j] # Schortcut for swapping

                #Swapping using temp variable
                # temp =arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = temp

                print(arr) # Printing with steps

arr = [5, 3, 8, 6, 7, 2]
bubbleSort(arr)
print('Array after sorting is: ', arr)

# arr = array('i', [])
# n = int(input("Enter the length the array: "))
# for i in range(n):
#     x = int(input("Enter the elements: "))
#     arr.append(x)
# print(arr)

# Output with steps:
# [3, 5, 8, 6, 7, 2]
# [3, 5, 6, 8, 7, 2]
# [3, 5, 6, 7, 8, 2]
# [3, 5, 6, 7, 2, 8]
# [3, 5, 6, 2, 7, 8]
# [3, 5, 2, 6, 7, 8]
# [3, 2, 5, 6, 7, 8]
# [2, 3, 5, 6, 7, 8]
# Array after sorting is:  [2, 3, 5, 6, 7, 8]