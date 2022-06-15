# Largest Sum Contiguous Subarray -> Kadane's Algorithm
# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
# Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers that has the largest sum. 
# Initialize:
#     max_so_far = INT_MIN
#     max_ending_here = 0

# Loop for each element of the array
#   (a) max_ending_here = max_ending_here + a[i]
#   (b) if(max_so_far < max_ending_here)
#             max_so_far = max_ending_here
#   (c) if(max_ending_here < 0)
#             max_ending_here = 0
# return max_so_far

## Algorithmic Paradigm: Dynamic Programming
## Time Complexity: O(n) 
def maxSubArraySum(arr, N):
        ##Your code here
        max_sum = curr_sum = arr[0]
        for i in range(1, N):
            curr_sum = max(arr[i], arr[i] + curr_sum)
            max_sum = max(max_sum, curr_sum)
        return max_sum

## Driver Code
arr = [-4, -1, 3, 5, -6, 7, 8, -1]
print("Maximum contiguous array: ", maxSubArraySum(arr, len(arr)))

# Output
# Maximum contiguous array:  17
# Starting Index 2
# Ending Index 6
# max = 3 + 5 + (-6) + 7 + 8 == 17