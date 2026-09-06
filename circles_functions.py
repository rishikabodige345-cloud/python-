import math

# Function to calculate the area of a circle
def calculate_area(radius):
    """
    Returns the area of a circle given its radius.
    Formula: π * r^2
    """
    return math.pi * radius ** 2


# Function to calculate the circumference of a circle
def calculate_circumference(radius):
    """
    Returns the circumference of a circle given its radius.
    Formula: 2 * π * r
    """
    return 2 * math.pi * radius


# Main function to call the above functions
def main():
    radius = 5  # You can change this value
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)

    print(f"Radius: {radius}")
    print(f"Area of the circle: {area}")
    print(f"Circumference of the circle: {circumference}")


# Run the program
if __name__ == "__main__":
    main()
