# 1 Check whether a number is positive, negative, or zero
n=int(input("Enter number: "))
if n>0:print("Positive")
elif n<0:print("Negative")
else:print("Zero")

# 2 Check whether a number is even or odd
n=int(input("Enter number: "))
if n%2==0:print("Even")
else:print("Odd")

# 3 Find the largest of two numbers
a=int(input("Enter first: "))
b=int(input("Enter second: "))
print(a if a>b else b)

# 4 Find the largest of three numbers
a=int(input("Enter first: "))
b=int(input("Enter second: "))
c=int(input("Enter third: "))
print(max(a,b,c))

# 5 Check whether a person is eligible to vote (age ≥ 18)
age=int(input("Enter age: "))
print("Eligible" if age>=18 else "Not Eligible")

# 6 Assign grades based on marks (A, B, C, Fail)
marks=int(input("Enter marks: "))
if marks>=75:print("A")
elif marks>=60:print("B")
elif marks>=35:print("C")
else:print("Fail")

# 7 Check whether a character is vowel or consonant
ch=input("Enter character: ")
if ch.lower() in "aeiou":print("Vowel")
else:print("Consonant")

# 8 Check whether a number is divisible by both 3 and 5
n=int(input("Enter number: "))
print("Divisible by 3 and 5" if n%3==0 and n%5==0 else "Not divisible")

# 9 Check whether a character is uppercase, lowercase, digit, or special symbol
ch=input("Enter character: ")
if ch.isupper():print("Uppercase")
elif ch.islower():print("Lowercase")
elif ch.isdigit():print("Digit")
else:print("Special Symbol")

# 10 Check whether a number is divisible by 7
n=int(input("Enter number: "))
print("Divisible by 7" if n%7==0 else "Not divisible")

# 11 Check whether a person is a senior citizen (age ≥ 60)
age=int(input("Enter age: "))
print("Senior Citizen" if age>=60 else "Not Senior Citizen")

# 12 Check whether a year is a leap year
year=int(input("Enter year: "))
if (year%400==0) or (year%4==0 and year%100!=0):print("Leap Year")
else:print("Not Leap Year")

# 13 Build a simple calculator (+,-,*,/)
a=int(input("Enter first: "))
b=int(input("Enter second: "))
op=input("Enter operator (+,-,*,/): ")
if op=="+":print(a+b)
elif op=="-":print(a-b)
elif op=="*":print(a*b)
elif op=="/":print(a/b)
else:print("Invalid")

# 14 Check whether a number is in range (1 to 100)
n=int(input("Enter number: "))
print("In Range" if 1<=n<=100 else "Out of Range")

# 15 Input marks of 3 subjects and check pass/fail (≥35 each)
m1=int(input("Enter mark1: "))
m2=int(input("Enter mark2: "))
m3=int(input("Enter mark3: "))
print("Pass" if m1>=35 and m2>=35 and m3>=35 else "Fail")

# 16 Check whether a number is a multiple of 3 and 5 (separately)
n=int(input("Enter number: "))
if n%3==0:print("Multiple of 3")
if n%5==0:print("Multiple of 5")

# 17 Simulate ATM withdrawal (check sufficient balance)
balance=1000
amt=int(input("Enter withdrawal amount: "))
if amt<=balance:balance-=amt;print("Withdrawn, Balance:",balance)
else:print("Insufficient Balance")

# 18 Calculate tax based on salary slabs
salary=int(input("Enter salary: "))
if salary<=250000:print("No Tax")
elif salary<=500000:print("Tax:",salary*0.05)
elif salary<=1000000:print("Tax:",salary*0.2)
else:print("Tax:",salary*0.3)

# 19 Check whether a number is a 3-digit number
n=int(input("Enter number: "))
print("3-digit" if 100<=n<=999 else "Not 3-digit")

# 20 Check whether a character is an alphabet (without built-in functions)
ch=input("Enter character: ")
if ('a'<=ch<='z') or ('A'<=ch<='Z'):print("Alphabet")
else:print("Not Alphabet")

# 21 Find the largest of three numbers using nested if
a=int(input("Enter first: "))
b=int(input("Enter second: "))
c=int(input("Enter third: "))
if a>b:
    if a>c:print(a)
    else:print(c)
else:
    if b>c:print(b)
    else:print(c)

# 22 Create a login system (username & password check)
user=input("Enter username: ")
pwd=input("Enter password: ")
if user=="admin" and pwd=="1234":print("Login Successful")
else:print("Login Failed")

# 23 Check whether a number is positive → then check even/odd
n=int(input("Enter number: "))
if n>0:
    if n%2==0:print("Positive Even")
    else:print("Positive Odd")
else:print("Not Positive")

# 24 ATM system with conditions (balance + withdrawal limit)
balance=2000
limit=1000
amt=int(input("Enter withdrawal amount: "))
if amt<=balance and amt<=limit:balance-=amt;print("Withdrawn, Balance:",balance)
else:print("Cannot Withdraw")

# 25 Student result system
marks=int(input("Enter marks: "))
if marks>=75:print("Distinction")
elif marks>=60:print("First Class")
elif marks>=35:print("Pass")
else:print("Fail")
