# 1. Check whether a number is positive
num = 5
if num > 0:
    print("positive")

# 2. Check if a person's age is 18 or above
age = 20
if age >= 18:
    print("Eligible to Vote")

# 3. Check whether a number is even or odd
num = 7
if num % 2 == 0:
    print("even")
else:
    print("odd")

# 4. Compare two numbers and print the larger
num1 = 10
num2 = 20
if num1 > num2:
    print(num1, "is greater")
else:
    print(num2)

# 5. Pass or Fail (marks >= 35)
marks = 30
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# 6. Leap year check (divisible by 4)
year = 2024
if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# 7. Divisible by 5
num = 25
if num % 5 == 0:
    print("Divisible by 5")

# 8. Vowel or consonant
ch = "i"
if ch in "aeiou":
    print("vowel")
else:
    print("consonant")

# 9. Positive, Negative, Zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

# 10. Assign grades
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade F")

# 11. Age category
age = 25
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# 12. Largest of three numbers
a = 10
b = 20
c = 30
d = 2
if a > b and a > c and a > d:
    print(a)
elif b > a and b > c and b > d:
    print(b)
elif c > d:
    print(c)

# 13. Multiple of 3 and 5
num = 30
if num % 3 == 0 and num % 5 == 0:
    print("The number is a multiple of both 3 and 5")
else:
    print("The number is not a multiple of both 3 and 5")

# 14. Password check
password = "python123"
if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

# 15. Day of the week
day = 4
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Day")

# 16. Discount
amount = 5000
if amount >= 5000:
    print("20% Discount")
elif amount >= 2000:
    print("10% Discount")
else:
    print("No Discount")

# 17. Season by month
month = 7
if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month == 3 or month == 4 or month == 5:
    print("Summer")
elif month == 6 or month == 7 or month == 8:
    print("Rainy")
elif month == 9 or month == 10 or month == 11:
    print("Autumn")
else:
    print("Invalid Month")

# 18. Electricity bill category
units = 250
if units <= 100:
    print("Low Usage")
elif units <= 300:
    print("Medium Usage")
else:
    print("High Usage")

# 19. Divisible by 2 or 3
num = 12
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both")
elif num % 2 == 0:
    print("Divisible by 2")
elif num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 2 or 3")
