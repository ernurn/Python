# Operators in Python

# Arithmetic Operators

print(5 + 2)    # add
print(5 - 2)    # subtraction
print(5 * 2)    # Multiplication
print(5 / 2)    # Division
print(5 % 2)    # Modulus
print(5 // 2)   # Floor division
print(5 ** 2)   # Exponentiation

# Coparative Operators
print(3 == 4)   # Equal
print(3 != 4)   # Not equal
print(3 > 4)    # Greater than
print(3 < 4)    # Less than
print(3 >= 4)   # Greater than or equal to
print(3 <= 4)   # Less than or equal to

print("Hello" == "Python")   # Equal
print("Hello" != "Python")   # Not equal
print("Hello" > "Python")    # Greater than
print("Hello" < "Python")    # Less than
print("Hello">= "Python")   # Greater than or equal to
print("Hello"<= "Python")   # Less than or equal to

# Logics Operators
print(3 > 4 and 4 == 4)     # and is TRUE if both are TRUE
print(3 > 4 or 4 == 4)      # or is TRUE if one of them is TRUE


# Strings Operators
print('Hello' + 'Python')   # Concatenate


# Calculating area of a circle
radius = 45     # radius of a circle
area_of_circle = 3.14 * radius ** 2     # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 30
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 85
gravity = 9.81
weight = mass * gravity
print(weight, 'N')  # Adding unit to the weight

# Calculate the density of a liquid
mass = 75       # in Kg
volume = 0.075  # in cubic meter
density = mass / volume
print('Density', density, 'Kg/m^3')

### Exercises ###
# 1 Declare your age as integer variable
age = int(38)
print('Age:', age)

# 2 Declare your height as a float variable
height = float(73.5)
print('Height:', height, 'mts')

# 3 Declare a variable that store a complex number
num = complex(1 + 1j)
print(num)

# 4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle.
base =  float(input('Enter base of triangle: '))
height = float(input('Entre height of triangle: '))
area = 0.5 * base * height
print('Area of triangle: ', area)

# 5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle.
