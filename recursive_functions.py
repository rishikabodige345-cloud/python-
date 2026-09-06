# Recursive function to calculate factorial
def factorial(n):
    """
    Returns the factorial of a non-negative integer n using recursion.
    Base case: factorial(0) = 1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Recursive function to calculate nth Fibonacci number
def fib(n):
    """
    Returns the nth Fibonacci number using recursion.
    Base cases: fib(0) = 0, fib(1) = 1
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Recursive function to sum digits of a number
def sum_digits(num):
    """
    Returns the sum of digits of a non-negative integer num using recursion.
    Base case: if num < 10, return num
    """
    if num < 10:
        return num
    else:
        return num % 10 + sum_digits(num // 10)


# Recursive function to reverse a string
def reverse_string(s):
    """
    Returns the reverse of string s using recursion.
    Base case: empty string or single character
    """
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


# Optional recursive function to check palindrome
def is_palindrome(s):
    """
    Returns True if string s is a palindrome using recursion.
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


# Main function to test all recursive functions
def main():
    print("Factorial of 5:", factorial(5))
    print("Fibonacci of 6:", fib(6))
    print("Sum of digits of 12345:", sum_digits(12345))
    print("Reverse of 'hello':", reverse_string("hello"))
    print("Is 'madam' a palindrome?:", is_palindrome("madam"))


# Run the program
if __name__ == "__main__":
    main()

