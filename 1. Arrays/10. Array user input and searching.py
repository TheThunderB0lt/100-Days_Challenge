## Getting array user input & searching index of the given array

from array import *

arr = array('i', []) # array user input
n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the elements: "))
    arr.append(x) # array elements adding
print(arr)

val = int(input("enter the element to search: "))

# algorithm for searching index value
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k+=1

print("Index is: ", arr.index(val)) # shortcut method using index() in python

# Output
# Enter the length of the array: 4  
# Enter the elements: 4  
# Enter the elements: 55
# Enter the elements: 33 
# Enter the elements: 12 
# array('i', [4, 55, 33, 12])
# enter the element to search: 33
# Index is: 2