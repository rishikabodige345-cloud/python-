# 1. Check whether a number is positive
num = 5
if num > 0:
    print("positive")

# 2. Check if age is 18 or above
age = 20
if age >= 18:
    print("Eligible to Vote")

# 3. Check even or odd
num = 7
if num % 2 == 0:
    print("even")
else:
    print("odd")

# 4. Compare two numbers
num1 = 10
num2 = 20
if num1 > num2:
    print(num1, "is greater")
else:
    print(num2)

# 5. Pass or Fail
marks = 30
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# 6. Leap year check
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

# 13. Multiple
