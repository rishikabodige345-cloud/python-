print("Section 1: Functions Without Parameters")

def welcome():print("Welcome to Python Programming")
def display_details():print("Name: Pavan, Age: 20, City: Hyderabad")
def show_even_numbers():
    for i in range(1,21):
        if i%2==0:print(i,end=" ")
    print()
def multiplication_table():
    for i in range(1,11):print("5 x",i,"=",5*i)

welcome()
display_details()
show_even_numbers()
multiplication_table()

print("Section 2: Functions With Parameters")

def greet(name):print("Hello",name)
def add(a,b):print("Sum:",a+b)
def find_square(n):print("Square:",n*n)
def find_greatest(a,b,c):print("Greatest:",max(a,b,c))

greet("Ravi")
add(10,20)
find_square(7)
find_greatest(12,45,30)

print("Section 3: Functions Using return")

def add_return(a,b):return a+b
def is_even(n):return n%2==0
def find_factorial(n):
    f=1
    for i in range(1,n+1):f=f*i
    return f
def calculate_area(length,breadth):return length*breadth

print("Sum:",add_return(5,6))
print("Is Even:",is_even(10))
print("Factorial:",find_factorial(5))
print("Area:",calculate_area(10,20))

print("Section 4: Positional Arguments")

def student_details(name,age,course):print("Name:",name,"Age:",age,"Course:",course)
def calculate_bill(item,price,quantity):return price*quantity
def employee_details(name,department,salary):print("Name:",name,"Department:",department,"Salary:",salary)

student_details("Ravi",21,"Python")
print("Bill:",calculate_bill("Pen",10,5))
employee_details("Anil","HR",30000)

print("Section 5: Default Arguments")

def greet_default(name,message="Good Morning"):print("Hello",name,message)
def calculate_simple_interest(principal,rate=5,time=2):return (principal*rate*time)/100

greet_default("Ravi")
greet_default("Ravi","Good Evening")
print("SI:",calculate_simple_interest(10000))
print("SI:",calculate_simple_interest(10000,10))
print("SI:",calculate_simple_interest(10000,10,3))

print("Section 6: Keyword Arguments")

def student_details_kw(name,age,course):print("Name:",name,"Age:",age,"Course:",course)
def product_details(product,price,quantity):return price*quantity

student_details_kw(age=20,course="Python",name="Ravi")
print("Total Price:",product_details(price=100,quantity=2,product="Book"))

print("Section 7: Mixed Challenge — All Concepts")

def calculate_salary(name,basic_salary,bonus=5000):return basic_salary+bonus

print("Salary:",calculate_salary("Ravi",30000,7000)) # positional
print("Salary:",calculate_salary(name="Anil",basic_salary=25000,bonus=6000)) # keyword
print("Salary:",calculate_salary("Pavan",40000)) # default bonus
