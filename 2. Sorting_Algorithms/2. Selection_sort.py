# Selection Sort
# In this algorithm, we create two segments of the list one sorted and the other unsorted. We continuously remove 
# the smallest element from the unsorted segment of the list and append it to the sorted segment. We don’t swap 
# intermediate elements. Hence this algorithm sorts the array in the minimum number of swaps

# Selection Sort is a more efficient algorithm than bubble sort. 
# Sort has a Time-Complexity of O(n2) in the average, worst, and in the best cases.

def selectionSort(arr):

    for i in range(len(arr)):
        minpos = i

        for j in range(i+1, len(arr)):
            
            if arr[j] < arr[minpos]:
                minpos = j

            arr[i], arr[minpos] = arr[minpos], arr[i]   # Shortcut method for swapping

            #by using temp variable 
            # temp = arr[i]
            # arr[i] = arr[minpos]
            # arr[minpos] = temp

            print(arr) # Printing with steps

arr = [5, 3, 8, 6, 7, 2]
selectionSort(arr)
print('Array after sorting is: ', arr)

# Output with steps:
# [3, 5, 8, 6, 7, 2]
# [5, 3, 8, 6, 7, 2]
# [3, 5, 8, 6, 7, 2]
# [5, 3, 8, 6, 7, 2]
# [2, 3, 8, 6, 7, 5]
# [2, 3, 8, 6, 7, 5]
# [2, 3, 8, 6, 7, 5]
# [2, 3, 8, 6, 7, 5]
# [2, 3, 8, 6, 7, 5]
# [2, 3, 6, 8, 7, 5]
# [2, 3, 7, 8, 6, 5]
# [2, 3, 5, 8, 6, 7]
# [2, 3, 5, 6, 8, 7]
# [2, 3, 5, 7, 8, 6]
# [2, 3, 5, 7, 6, 8]
# Array after sorting is:  [2, 3, 5, 7, 6, 8]