
### 1. Check whether a character is vowel or consonant

```python
ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")
```

### 2. Check whether a number is divisible by both 3 and 5

```python
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")
```

### 3. Check whether a character is uppercase, lowercase, digit, or special symbol

```python
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")
```

### 4. Check whether a number is divisible by 7

```python
num = int(input("Enter a number: "))

if num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")
```

### 5. Check whether a person is a senior citizen

```python
age = int(input("Enter age: "))

if age >= 60:
    print("Senior Citizen")
else:
    print("Not a Senior Citizen")
```

### 6. Check whether a year is a leap year

Since your assignment says to assume the year is divisible by 4:

```python
year = int(input("Enter year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
```

### 7. Simple calculator (+, -, *, /)

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Operator")
```

### 8. Check whether a number is in the range 1 to 100

```python
num = int(input("Enter a number: "))

if num >= 1 and num <= 100:
    print("Number is in the range 1 to 100")
else:
    print("Number is not in the range 1 to 100")
```

### 9. Input marks of 3 subjects and check pass/fail

A student passes only if **all three subjects are 35 or above**.

```python
mark1 = int(input("Enter marks of subject 1: "))
mark2 = int(input("Enter marks of subject 2: "))
mark3 = int(input("Enter marks of subject 3: "))

if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    print("Pass")
else:
    print("Fail")
```

### 10. Check whether a number is a multiple of 3 and 5 separately

```python
num = int(input("Enter a number: "))

if num % 3 == 0:
    print("Multiple of 3")
else:
    print("Not a multiple of 3")

if num % 5 == 0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")
```

### 11. Simulate ATM withdrawal

```python
balance = 10000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    balance = balance - amount
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)
else:
    print("Insufficient Balance")
```

### 12. Calculate tax based on salary slabs

If your assignment doesn't specify different slabs, a common simple version is:

```python
salary = float(input("Enter salary: "))

if salary <= 250000:
    tax = 0
elif salary <= 500000:
    tax = salary * 0.05
elif salary <= 1000000:
    tax = salary * 0.20
else:
    tax = salary * 0.30

print("Tax =", tax)
```

