# 6. All types of Prime Numbers coding


# Method 1: Check Wheater Number is prime or not
num = int(input("Enter the number: "))
if num > 1:
    for i in range(2, num):
        if (num%i) == 0:
            print(num, "is Not a prime Number")
            break
    else:
        print(num, "is Prime Number")
else:
    print(num, "Not a prime Number")

# OUTPUT:
# Enter the number: 11
# 11 is Prime Number

# Enter the number: 16
# 16 is Not a Prime Number


# Method 2: Prime numbers from 1-100
for num in range(1, 100):
    if num > 1:
        for i in range(2, num):
            if(num%i) == 0:
                break
        else:
            print(num, end=" | ")

# OUTPUT:
# 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 | 41 | 43 | 47 | 53 | 59 | 61 | 67 | 71 | 73 | 79 | 83 | 89 | 97 | 


# Method 3: Prime no: giving range
start = int(input("Enter the start range: "))
end = int(input("Enter the final range: "))

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=" | ")

# OUTPUT:
# Enter the start range: 1
# Enter the final range: 100
# 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 | 41 | 43 | 47 | 53 | 59 | 61 | 67 | 71 | 73 | 79 | 83 | 89 | 97 | 