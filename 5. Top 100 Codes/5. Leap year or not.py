# 5. Checking Leap year or not

# Input : 2020
# Output : It's a Leap Year.

# Conditions for a Leap Year
# Here are the two conditions that any year must satisfy to be called a leap year
# 1. The year must be perfectly divisible by 400.
# 2. The number must be divisible by 4 but not by 100.

year = int(input("Enter the Year: "))

if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print(year, "is Leap year")
else:
    print(year, "is not a Leap year")

