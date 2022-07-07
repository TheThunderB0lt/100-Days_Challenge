# 3. Sum of first N natural number

# Input : num = 8
# Output : 36

# Where first 8 number is 1, 2, 3, 4, 5, 6, 7, 8
# Sum of numbers = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36

# Method 1: for loop
num = int(input("Enter the Number: "))
sum = 0
for i in range(num + 1):
    sum += i
print(sum)


# Method 2: using formula (n*(n+1)/2)
num = int(input("Enter the Number: "))
print("", int(num * (num + 1) / 2))


