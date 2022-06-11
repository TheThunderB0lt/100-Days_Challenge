# Program to finding an element in an array based on user input

arr =[23, 44, 56, 78, 34, 22, 65, 67]
inp = input("Enter number for searching: ")
for i in range(1,len(arr),1):
    if int(inp) == arr[i] :
        print("The index of that number is: ", i)

# OP: Enter number : 78
# The index of that number is:  3
