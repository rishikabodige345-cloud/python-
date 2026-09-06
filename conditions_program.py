print("Assignment Program - All Questions")

#1 Positive/Negative/Zero
num=int(input("Enter number: "))
if num>0:print("Positive")
elif num<0:print("Negative")
else:print("Zero")

#2 Even/Odd
num=int(input("Enter number: "))
if num%2==0:print("Even")
else:print("Odd")

#3 Largest of Two
a=int(input("Enter first: "))
b=int(input("Enter second: "))
print("Largest:",a if a>b else b)

#4 Largest of Three
a=int(input("Enter first: "))
b=int(input("Enter second: "))
c=int(input("Enter third: "))
print("Largest:",max(a,b,c))

#5 Eligible to Vote
age=int(input("Enter age: "))
print("Eligible" if age>=18 else "Not eligible")

#6 Assign Grades
marks=int(input("Enter marks: "))
if marks>=75:print("Grade A")
elif marks>=60:print("Grade B")
elif marks>=40:print("Grade C")
else:print("Fail")

#7 Vowel or Consonant
ch=input("Enter character: ").lower()
print("Vowel" if ch in "aeiou" else "Consonant")

#8 Divisible by 3 and 5
num=int(input("Enter number: "))
print("Divisible" if num%3==0 and num%5==0 else "Not divisible")

#9 Character Classification
ch=input("Enter character: ")
if ch.isupper():print("Uppercase")
elif ch.islower():print("Lowercase")
elif ch.isdigit():print("Digit")
else:print("Special symbol")

#10 Divisible by 7
num=int(input("Enter number: "))
print("Divisible by 7" if num%7==0 else "Not divisible")

#11 Senior Citizen Check
age=int(input("Enter age: "))
print("Senior Citizen" if age>=60 else "Not Senior Citizen")

#12 Leap Year Check
year=int(input("Enter year: "))
if year%400==0 or (year%4==0 and year%100!=0):print("Leap Year")
else:print("Not Leap Year")

#13 Simple Calculator
a=float(input("Enter first: "))
b=float(input("Enter second: "))
op=input("Enter operator: ")
if op=='+':print(a+b)
elif op=='-':print(a-b)
elif op=='*':print(a*b)
elif op=='/':print(a/b if b!=0 else "Division by zero")
else:print("Invalid operator")

#14 Range 1-100
num=int(input("Enter number: "))
print("In range" if 1<=num<=100 else "Out of range")

#15 Pass/Fail (3 Subjects)
m1=int(input("Enter marks1: "))
m2=int(input("Enter marks2: "))
m3=int(input("Enter marks3: "))
print("Pass" if m1>=35 and m2>=35 and m3>=35 else "Fail")

#16 Multiple of 3 and 5
num=int(input("Enter number: "))
print("Multiple of 3" if num%3==0 else "Not multiple of 3")
print("Multiple of 5" if num%5==0 else "Not multiple of 5")

#17 ATM Withdrawal
balance=int(input("Enter balance: "))
withdraw=int(input("Enter withdrawal: "))
print("Success" if withdraw<=balance else "Insufficient balance")

#18 Tax Calculation
salary=int(input("Enter salary: "))
if salary<=250000:tax=0
elif salary<=500000:tax=salary*0.05
elif salary<=1000000:tax=salary*0.2
else:tax=salary*0.3
print("Tax:",tax)

#19 3-digit Number Check
num=int(input("Enter number: "))
print("3-digit" if 100<=num<=999 else "Not 3-digit")

#20 Alphabet Check
ch=input("Enter character: ")
if ('a'<=ch<='z') or ('A'<=ch<='Z'):print("Alphabet")
else:print("Not alphabet")

#21 Largest of Three (Nested If)
a=int(input("Enter first: "))
b=int(input("Enter second: "))
c=int(input("Enter third: "))
if a>b:
    if a>c:print("Largest:",a)
    else:print("Largest:",c)
else:
    if b>c:print("Largest:",b)
    else:print("Largest:",c)

#22 Login System
u=input("Enter username: ")
p=input("Enter password: ")
print("Login success" if u=="admin" and p=="1234" else "Login failed")

#23 Positive → Even/Odd
num=int(input("Enter number: "))
if num>0:
    print("Positive")
    print("Even" if num%2==0 else "Odd")
else:print("Not positive")

#24 ATM System with Conditions
balance=int(input("Enter balance: "))
withdraw=int(input("Enter withdrawal: "))
limit=int(input("Enter limit: "))
print("Success" if withdraw<=balance and withdraw<=limit else "Failed")

#25 Student Result System
marks=int(input("Enter marks: "))
if marks>=75:print("Distinction")
elif marks>=60:print("First Class")
elif marks>=35:print("Pass")
else:print("Fail")
