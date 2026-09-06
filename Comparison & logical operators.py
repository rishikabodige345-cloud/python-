# Comparison Operators (==, !=, >, <, >=, <=)

# Q1. Rahul scored 78 marks. The passing mark is 35.
# Write a Python expression to check whether Rahul passed.
marks = 78
passing_mark = 35
print("Q1:", marks >= passing_mark)

# Q2. A movie ticket is allowed only for people aged 18 or above.
# A person's age is 16. Write an expression to check if they are eligible.
age = 16
print("Q2:", age >= 18)

# Q3. A laptop costs ₹55,000. Your budget is ₹60,000.
# Check whether the laptop is within your budget.
laptop_cost = 55000
budget = 60000
print("Q3:", laptop_cost <= budget)

# Q4. There are 25 students in Class A and 25 students in Class B.
# Write an expression to check whether both classes have the same number of students.
classA = 25
classB = 25
print("Q4:", classA == classB)

# Q5. The temperature today is 42°C.
# Check whether the temperature is greater than 40°C.
temperature = 42
print("Q5:", temperature > 40)

# Q6. A customer entered the correct OTP 5678. The entered OTP is 6789.
# Write an expression to check whether the OTP is incorrect.
correct_otp = 5678
entered_otp = 6789
print("Q6:", correct_otp != entered_otp)

# Q7. The speed limit is 80 km/h. A car is moving at 80 km/h.
# Check whether the car is following the speed limit.
speed_limit = 80
car_speed = 80
print("Q7:", car_speed == speed_limit)

# Q8. A train has 150 seats. Currently, 145 seats are booked.
# Check whether all seats are filled.
total_seats = 150
booked = 145
print("Q8:", booked == total_seats)

# Q9. The minimum balance required in a bank account is ₹1000.
# Current balance is ₹850. Check whether the balance is less than the required amount.
min_balance = 1000
current_balance = 850
print("Q9:", current_balance < min_balance)

# Q10. A student needs at least 75% attendance. Current attendance is 75%.
# Check whether the student is eligible for the exam.
attendance_required = 75
attendance = 75
print("Q10:", attendance >= attendance_required)


# Logical Operators (and, or, not)

# Q11. Placement drive eligibility: CGPA ≥ 7.5 AND Attendance ≥ 75%.
cgpa = 8.1
attendance = 82
print("Q11:", cgpa >= 7.5 and attendance >= 75)

# Q12. Free delivery if purchase > 500 OR Prime member.
purchase = 650
prime_member = True
print("Q12:", purchase > 500 or prime_member)

# Q13. Login if username correct OR email correct.
username_correct = False
email_correct = True
print("Q13:", username_correct or email_correct)

# Q14. Cricket player selected if runs > 500 AND wickets > 20.
runs = 620
wickets = 18
print("Q14:", runs > 500 and wickets > 20)

# Q15. Student passes if theory ≥ 35 AND practical ≥ 35.
theory = 40
practical = 30
print("Q15:", theory >= 35 and practical >= 35)

# Q16. Discount if member OR purchase > 2000.
member = False
purchase = 2500
print("Q16:", member or purchase > 2000)

# Q17. Vote if age ≥ 18 AND citizen = True.
age = 20
citizen = True
print("Q17:", age >= 18 and citizen)

# Q18. Student is not absent.
absent = False
print("Q18:", not absent)

# Q19. Admin access if username = "admin" AND password correct.
username = "admin"
password_correct = True
print("Q19:", username == "admin" and password_correct)

# Q20. Swimming pool entry if membership OR paid fee.
membership = False
paid_fee = False
print("Q20:", membership or paid_fee)


# Mixed Comparison + Logical Operators

# Q21. Grade A if marks between 90 and 100.
marks = 95
print("Q21:", marks >= 90 and marks <= 100)

# Q22. Cashback if purchase between 1000 and 5000.
purchase = 3200
print("Q22:", purchase >= 1000 and purchase <= 5000)

# Q23. Reset password if OTP correct AND account active.
otp_correct = True
account_active = True
print("Q23:", otp_correct and account_active)

# Q24. Player qualifies if age between 18 and 25.
age = 23
print("Q24:", age >= 18 and age <= 25)

# Q25. Vehicle fined if speed > 80 OR signal broken.
speed = 75
signal_broken = True
print("Q25:", speed > 80 or signal_broken)


# Challenge Questions

# Q26. Number between 10 and 50.
num = 25
print("Q26:", num >= 10 and num <= 50)

# Q27. Person is student OR teacher.
is_student = True
is_teacher = False
print("Q27:", is_student or is_teacher)

# Q28. Password length ≥ 8 AND contains digit.
password = "abc12345"
print("Q28:", len(password) >= 8 and any(ch.isdigit() for ch in password))

# Q29. Age not less than 18.
age = 20
print("Q29:", not (age < 18))

# Q30. Gift if purchase > 5000 AND premium member AND birthday.
purchase = 6000
premium_member = True
birthday = True
print("Q30:", purchase > 5000 and premium_member and birthday)
