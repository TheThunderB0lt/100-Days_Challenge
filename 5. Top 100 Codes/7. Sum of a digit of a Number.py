# 7. Sum of a digit of a Number

# Input : number = 123
# Output : 6

# Method 1: Using String Extraction method
num = input("Enter the Numbers: ")
sum = 0
 
for i in num:
    sum = sum + int(i)
    
print("The sum of digit is: ", sum)

# Method 2: Using Brute Force
num = int(input("Enter the Numbers: "))
sum = 0
while num != 0:
    digit = int(num % 10)
    sum += digit
    num = num/10

print("The sum of digit is: ", sum)

# OUTPUT:
# Enter the Numbers: 1233
# The sum of digit is:  9

