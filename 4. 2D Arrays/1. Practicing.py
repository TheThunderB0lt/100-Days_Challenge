# 1. Traversing Values in Python 2D Array

arr = [[1,2,3],[4,5,6],[7,8,9]]
for i in arr:
    for j in i:
        print(j, end=" ")
    print()
# OUTPUT:
# 1 2 3 
# 4 5 6 
# 7 8 9 


# 2. Inserting values in inner array

arr = [[1,2,3],[4,5,6],[7,8,9]]
arr[1].insert(2, 13)
for i in arr:
    for j in i:
        print(j, end=" ")
    print()

# OUTPUT
# 1 2 3 
# 4 5 13 6 
# 7 8 9 

# 3. Inserting values in outer array

arr = [[1,2,3],[4,5,6],[7,8,9]]
arr.insert(3, [11,12,13])
for i in arr:
    for j in i:
        print(j, end=" ")
    print()

# OUTPUT
# 1 2 3 
# 4 5 6 
# 7 8 9 
# 11 12 13 

# $. Deleting an array in inner 

arr = [[1,2,3],[4,5,6],[7,8,9]]
del(arr[2][1])
for i in arr:
    for j in i:
        print(j, end=" ")
    print()

# OUTPUT:
# 1 2 3 
# 4 5 6 
# 7 9 