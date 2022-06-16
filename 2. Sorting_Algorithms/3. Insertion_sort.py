# Insertion Sort
# Like Selection Sort, in this algorithm, we segment the list into sorted and unsorted parts. Then we iterate over 
# the unsorted segment and insert the element from this segment into the correct position in the sorted list.

# Insertion Sort has a Time-Complexity of O(n2) in the average and worst case, and O(n) in the best case.

def insertionSort(arr):

    for i in range(1, len(arr)):
        j = i

        while arr[j-1] > arr[j] and j > 0: # checking left neighbour is gretter than or not
    
            arr[j-1], arr[j] = arr[j], arr[j-1] #Swapping
            j -= 1

        print(arr) #Printing with steps


arr = [5, 3, 8, 6, 7, 2]
insertionSort(arr)
print('Array after sorting is: ', arr)

# Output with steps:
# [3, 5, 8, 6, 7, 2]
# [3, 5, 8, 6, 7, 2]
# [3, 5, 6, 8, 7, 2]
# [3, 5, 6, 7, 8, 2]
# [2, 3, 5, 6, 7, 8]
# Array after sorting is:  [2, 3, 5, 6, 7, 8]