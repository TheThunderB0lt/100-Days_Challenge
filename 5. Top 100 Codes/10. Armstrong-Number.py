# # 10. Checking wheteher the number is Armstrong or Not

# abcd… = an + bn + cn + dn + …
# Where n is the order(length/digits in number)

# Number = 370 (order = 3)
# 370 = 3^3 + 7^3 + 0^3
# = 27 + 343 + 0
# = 370

num = int(input("Enter the number: ")) #user input

sum = 0 #Initialize Sum
order = len(str(num)) #Length of the given input numbers
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is Not an Armstrong number")

# OUTPUT:
# Enter the number: 370
# 370 is an Armstrong number