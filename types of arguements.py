```python
# Section 1: Functions Without Parameters

# Question 1
def welcome():
    print("Welcome to Python Programming")

welcome()


# Question 2
def display_details():
    print("Name: Ravi")
    print("Age: 20")
    print("City: Hyderabad")

display_details()


# Question 3
def show_even_numbers():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)

show_even_numbers()


# Question 4
def multiplication_table():
    for i in range(1, 11):
        print("5 x", i, "=", 5 * i)

multiplication_table()


# Section 2: Functions With Parameters

# Question 5
def greet(name):
    print("Hello", name)

greet("Ravi")


# Question 6
def add(a, b):
    print("Sum =", a + b)

add(10, 20)


# Question 7
def find_square(n):
    print("Square =", n * n)

find_square(5)


# Question 8
def find_greatest(a, b, c):
    if a >= b and a >= c:
        print("Greatest =", a)
    elif b >= a and b >= c:
        print("Greatest =", b)
    else:
        print("Greatest =", c)

find_greatest(10, 25, 15)


# Section 3: Functions Using return

# Question 9
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)


# Question 10
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

result = is_even(10)
print(result)


# Question 11
def find_factorial(n):
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

    return factorial

result = find_factorial(5)
print("Factorial =", result)


# Question 12
def calculate_area(length, breadth):
    return length * breadth

result = calculate_area(10, 5)
print("Area =", result)


# Section 4: Positional Arguments

# Question 13
def student_details(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_details("Ravi", 20, "BTech")


# Question 14
def calculate_bill(item, price, quantity):
    return price * quantity

result = calculate_bill("Pen", 10, 5)
print("Total Bill =", result)


# Question 15
def employee_details(name, department, salary):
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)

employee_details("Ravi", "IT", 30000)


# Section 5: Default Arguments

# Question 16
def greet(name, message="Good Morning"):
    print(message, name)

greet("Ravi")
greet("Ravi", "Good Evening")


# Question 17
def calculate_simple_interest(principal, rate=5, time=2):
    return (principal * rate * time) / 100

result1 = calculate_simple_interest(10000)
print("Only principal:", result1)

result2 = calculate_simple_interest(10000, 6)
print("Principal and rate:", result2)

result3 = calculate_simple_interest(10000, 6, 3)
print("Principal, rate and time:", result3)


# Section 6: Keyword Arguments

# Question 18
def student_details(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_details(course="BTech", name="Ravi", age=20)


# Question 19
def product_details(product, price, quantity):
    return price * quantity

result = product_details(
    quantity=5,
    product="Pen",
    price=10
)

print("Total Price =", result)


# Section 7: Mixed Challenge

# Question 20
def calculate_salary(name, basic_salary, bonus=5000):
    total_salary = basic_salary + bonus
    return total_salary


# Positional arguments
result1 = calculate_salary("Ravi", 30000, 3000)
print("Positional:", result1)


# Keyword arguments
result2 = calculate_salary(
    name="Ravi",
    basic_salary=30000,
    bonus=7000
)
print("Keyword:", result2)


# Default bonus
result3 = calculate_salary("Ravi", 30000)
print("Default Bonus:", result3)
```
