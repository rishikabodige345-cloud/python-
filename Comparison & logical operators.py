# Comparison Operators (==, !=, >, <, >=, <=)

# Q1
marks = 78
passing = 35
print("Q1:", marks >= passing)   # Rahul passed

# Q2
age = 16
print("Q2:", age >= 18)   # Eligible?

# Q3
laptop_cost = 55000
budget = 60000
print("Q3:", laptop_cost <= budget)   # Within budget?

# Q4
classA = 25
classB = 25
print("Q4:", classA == classB)   # Same number of students?

# Q5
temperature = 42
print("Q5:", temperature > 40)   # Hotter than 40°C?

# Q6
correct_otp = 5678
entered_otp = 6789
print("Q6:", correct_otp != entered_otp)   # OTP incorrect?

# Q7
speed_limit = 80
car_speed = 80
print("Q7:", car_speed == speed_limit)   # Following speed limit?

# Q8
total_seats = 150
booked = 145
print("Q8:", booked == total_seats)   # All seats filled?

# Q9
min_balance = 1000
current_balance = 850
print("Q9:", current_balance < min_balance)   # Balance less than required?

# Q10
attendance_required = 75
attendance = 75
print("Q10:", attendance >= attendance_required)   # Eligible for exam?


# Logical Operators (and, or, not)

# Q11
cgpa = 8.1
attendance = 82
print("Q11:", cgpa >= 7.5 and attendance >= 75)   # Placement eligibility?

# Q12
purchase = 650
prime_member = True
print("Q12:", purchase > 500 or prime_member)   # Free delivery?

# Q13
username_correct = False
email_correct = True
print("Q13:", username_correct or email_correct)   # Login allowed?

# Q14
runs = 620
wickets = 18
print("Q14:", runs > 500 and wickets > 20)   # Player selected?

# Q15
theory = 40
practical = 30
print("Q15:", theory >= 35 and practical >= 35)   # Student passed?

# Q16
member = False
purchase = 2500
print("Q16:", member or purchase > 2000)   # Discount?

# Q17
age = 20
citizen = True
print("Q17:", age >= 18 and citizen)   # Can vote?

# Q18
absent = False
print("Q18:", not absent)   # Student present?

# Q19
username = "admin"
password_correct = True
print("Q19:", username == "admin" and password_correct)   # Admin access?

# Q20
membership = False
paid_fee = False
print("Q20:", membership or paid_fee)   # Swimming pool entry?


# Mixed Comparison + Logical Operators

# Q21
marks = 95
print("Q21:", marks >= 90 and marks <= 100)   # Grade A?

# Q22
purchase = 3200
print("Q22:", purchase >= 1000 and purchase <= 5000)   # Cashback?

# Q23
otp_correct = True
account_active = True
print("Q23:", otp_correct and account_active)   # Reset password?

# Q24
age = 23
print("Q24:", age >= 18 and age <= 25)   # Player qualifies?

# Q25
speed = 75
signal_broken = True
print("Q25:", speed > 80 or signal_broken)   # Vehicle fined?


# Challenge Questions

# Q26
num = 25
print("Q26:", num >= 10 and num <= 50)   # Number between 10 and 50?

# Q27
is_student = True
is_teacher = False
print("Q27:", is_student or is_teacher)   # Student or teacher?

# Q28
password = "abc12345"
print("Q28:", len(password) >= 8 and any(ch.isdigit() for ch in password))   # Valid password?

# Q29
age = 20
print("Q29:", not (age < 18))   # Age not less than 18?

# Q30
purchase = 6000
premium_member = True
birthday = True
print("Q30:", purchase > 5000 and premium_member and birthday)   # Gift eligibility?
