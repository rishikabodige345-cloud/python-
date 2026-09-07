# 1.check Even or Odd
# Question: Determine whether a number is even or odd. Explanation: A number is even if it is divisible by 2. Otherwise, it’s odd. - Input: Number = 6 - Output: Even number
num=6
if num%2==0:
    print("even number")
else:
    print("odd number")




# 2. Divisible by 5 but Not by 10
# Question: Check if a number is divisible by 5 but not by 10. Explanation: Use modulo (%) to check if the number % 5 == 0 and number % 10 != 0. - Input: Number = 25 - Output: Satisfy
num=25
if num%5==0 and num%10!=0:
    print("satisfy")
else:
    print("not satisfy")




# 3. Biggest Among Two Numbers
# Question: Find the biggest number among two. Explanation: Use comparison operators (>) to check which number is greater. - Input: A = 4, B = 7 - Output: Biggest is: 7
a=4
b=7
if a>=b:
    print("a is bigger")
else:
    print("b is bigger")




# 4. Smallest Among Two Numbers
# Question: Find the smallest number among two. Explanation: Use comparison operators (<) to find the smaller value. - Input: A = 4, B = 7 - Output: Smallest is: 4
a=4
a=7
if a<b:
    print("a is smaller")
else:
    print("b is smaller")



    
# 5. Divisible by 2, 3, and 6
# Question: Check if a number is divisible by 2, 3, and 6. Explanation: If a number is divisible by both 2 and 3, it is also divisible by 6. - Input: Number = 18 - Output: Satisfy
num=18
if num%2==0 and num%3==0 and num%6==0:
    print("satisfy")
else:
    print("not satisfy")




# 6. Voting Eligibility
# Question: Check if a person is eligible to vote (age >= 18). Explanation: A person is eligible to vote if their age is 18 or above. - Input: Age = 19 - Output: Eligible to vote
age=18
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")




# 7. Student Pass/Fail Based on All Subjects >= 35
# Question: Check if a student passed all subjects (maths, physics, chemistry). Explanation: Student passes only if marks in all subjects are 35 or more. - Input: Maths = 40, Physics = 36, Chemistry = 30 - Output: Fail
maths=40
physics=36
chemistry=30
if maths>=35 and physics>=35 and chemistry>=35:
    print("pass")
else:
    print("fail")


    
# 8. Student Pass if Passed Any One Subject (>= 35)
# Question: Check if the student passed at least one subject. Explanation: Use logical OR to check if any one subject has marks >= 35. - Input: Maths = 20, Physics = 38, Chemistry = 25 - Output: Pass
maths=20
physics=38
chemistry=25
if maths>=35 and physics>=35 and chemistry>=35:
    print("pass")
else:
    print("fail")


    
# 9. Student Pass if Passed Any Two Subjects
# Question: Check if the student passed any two out of three subjects. Explanation: Use a counter or logical conditions to verify two subjects >= 35. - Input: Maths = 40, Physics = 20, Chemistry = 36 - Output: Pass
maths = 40
physics = 20
chemistry = 36
count = 0
if maths >= 35:
    count += 1
if physics >= 35:
    count += 1
if chemistry >= 35:
    count += 1
if count >= 2:
    print("Pass")
else:
    print("Fail")


    
# 10. Biggest Among Three Numbers
# Question: Find the biggest number among three. Explanation: Compare each pair of numbers using if-else conditions. - Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9
a = 7
b = 4
c = 9
if a >= b and a >= c:
    print("Biggest is:", a)
elif b >= a and b >= c:
    print("Biggest is:", b)
else:
    print("Biggest is:", c)


    
# 11. Smallest Among Three Numbers
# Question: Find the smallest number among three. Explanation: Use comparison logic to determine the minimum value. - Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4
a = 7
b = 4
c = 9
if a <= b and a <= c:
    print("Smallest is:", a)
elif b <= a and b <= c:
    print("Smallest is:", b)
else:
    print("Smallest is:", c)


    
# 12. Perfect Square or Not
# Question: Check if a number is a perfect square. Explanation: A number is a perfect square if the square of its square root equals the number. - Input: Number = 49 - Output: Perfect square
num = 49
root = int(num ** 0.5)
if root * root == num:
    print("Perfect square")
else:
    print("Not a perfect square")


    
# 13. Cars Required for Members (Max 5 per car)
# Question: Calculate how many cars are needed for a given number of people. Explanation: Divide total people by 5 and round up using ceiling logic. - Input: Members = 17 - Output: Cars needed = 4
members = 17
cars = (members + 4) // 5
print("Cars needed =", cars)



# 14. Second Biggest Among Three Numbers
# Question: Find the second largest number among three inputs. Explanation: Use sorting or nested conditions to find the second largest value. - Input: A = 10, B = 25, C = 18 - Output: Second biggest: 18
a = 10
b = 25
c = 18
if (a > b and a < c) or (a > c and a < b):
    print("Second biggest:", a)
elif (b > a and b < c) or (b > c and b < a):
    print("Second biggest:", b)
else:
    print("Second biggest:", c)


    
# 15. Leap Year or Not
# Question: Check if a given year is a leap year. Explanation: A year is a leap year if it is divisible by 4, and (not divisible by 100 unless divisible by 400). - Input: Year = 2024 - Output: Leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")










