
### 1. Check whether a number is positive

```python
num = 10

if num > 0:
    print("Positive")
```

### 2. Check if a person is eligible to vote

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
```

### 3. Check whether a number is even or odd

```python
num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 4. Compare two numbers and print the larger number

```python
num1 = 20
num2 = 15

if num1 > num2:
    print(num1, "is greater")
else:
    print(num2, "is greater")
```

### 5. Check whether a student passed or failed

```python
marks = 50

if marks >= 35:
    print("Pass")
else:
    print("Fail")
```

### 6. Check whether a year is a leap year

```python
year = 2024

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
```

### 7. Check whether a number is divisible by 5

```python
num = 25

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
```

### 8. Check whether a character is a vowel or consonant

```python
ch = "i"

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")
```

### 9. Check whether a number is positive, negative, or zero

```python
num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")
```

### 10. Assign grades based on marks

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade F")
```

### 11. Check whether a person is a child, teenager, adult, or senior citizen

```python
age = 25

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
```

### 12. Find the largest of three numbers

```python
a = 10
b = 20
c = 30

if a > b and a > c:
    print(a, "is largest")
elif b > a and b > c:
    print(b, "is largest")
else:
    print(c, "is largest")
```

### 13. Check whether a number is a multiple of both 3 and 5

```python
num = 30

if num % 3 == 0 and num % 5 == 0:
    print("The number is a multiple of both 3 and 5")
else:
    print("The number is not a multiple of both 3 and 5")
```

### 14. Check the password

```python
password = "python123"

if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")
```

### 15. Display the day of the week

```python
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
```

### 16. Calculate discount

```python
amount = 5000

if amount >= 5000:
    print("20% Discount")
elif amount >= 2000:
    print("10% Discount")
else:
    print("No Discount")
```

### 17. Determine the season based on month

```python
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
```

### 18. Electricity bill category

```python
units = 250

if units <= 100:
    print("Low Usage")
elif units <= 300:
    print("Medium Usage")
else:
    print("High Usage")
```

### 19. Check divisibility by 2 and 3

```python
num = 12

if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both")
elif num % 2 == 0:
    print("Divisible by 2")
elif num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 2 or 3")
```

