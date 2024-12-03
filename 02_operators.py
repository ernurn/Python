### Operators in Python ###

# Arithmetic Operators
'''
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
side_a = float(input('Enter side a:'))
side_b = float(input('Enter side b:'))
side_c = float(input('Enter side c:'))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is: ', perimeter)

# 6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter
length = float(input('Enter lenght: '))
weight = float(input('Enter weight: '))
area = length * weight
perimeter = (length + weight) * 2
print('The area of rectangle is: ', area)
print('The perimeter of the rectangle is: ', perimeter)

# 7 et radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference
radius = float(input('Enter radius of circle: '))
pi = 3.14
area = pi * radius ** 2
circumference = 2 * pi * radius
print('The area of ircle is: ', area)
print('The circumference of circle is: ', circumference)

# 8 Calculate the slope, x-intercept and y-intercept of y = 2x -2
print('y = 2x -2')
slope_1 = 2
print('Slope: ', slope_1)
# y-intercept whewn x = 0
x = 0
y = 2 * x - 2
print('Y-intercept', '(', x, ';', y, ')')

# x-intercept whewn y = 0
x = 2 / 2
y = 0
print('X-intercept', '(', x, ';', y, ')')

# 9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
point_x1 = 2
point_y1 = 2
point_x2 = 6
point_y2 = 10
slope_2 = (point_y2 - point_y1) / (point_x2 - point_x1)
euclidean_distance = ((point_x2 - point_x1)**2 + (point_y2 - point_y1)**2)**0.5
print('Slope: ', slope_2)
print('Euclidean distance: ', euclidean_distance)

# 10 Compare the slopes in tasks 8 and 9.
if slope_1 == slope_2:
    print('Equal')
else:
    print('not equal')

# 11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
y = 1
while y != 0:
    x = int(input('Insert x value:'))
    y = x ** 2 + 6*x + 9
    print('  x',' | ','y', '\n', '(', x , ';', y,')')


#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python'') == len('dragon'))


#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'dragon':
    print('yes')
else:
    print('no')


#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'
if 'jargon' in sentence:
    print('yes')
else:
    print('no')


15# There is no 'on' in both dragon and python
if 'on' not in 'python' and 'dragon':
    print('yes')
else:
    print('no')


16# Find the length of the text python and convert the value to float and convert it to string
text = 'python'
length = float(len(text))
print(length, 'as float')
print(type(length))
length = str(length)
print(length, 'as string')
print(type(length))


#17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print('Even number checker')
num = int(input('Insert a number:'))
if num % 2:
    print('The number is not even')
else: 
    print('Even number')



#18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
if 7 // 3 == int(2.7):
    print('are equal to 2')



#19 Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print('Are equals')
else:
    print('Are not equals')
    print (type('10'))
    print(type(10))


#20 Check if int('9.8') is equal to 10
float_value = float('9.8')
int_value = int(float_value)
if int_value == 10:
    print('Are equals')
else:
    print('Are not equals')
    print('float', float_value)
    print('int', int_value)
    print(10)



#21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
weekly_earning = hours * rate_per_hour
print('Your weekly earning is:', weekly_earning)



#22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
lived = int(input('Enter number of years you have lived:'))
print(f'You have lived for {lived * 31536000} seconds.')

'''

#23 Write a Python script that displays the following table
print('n 1 n n**2 n**3') #header of the table
for n in range(1,6):
    print(f'{n} 1 {n}  {n**2}   {n**3}')

'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''