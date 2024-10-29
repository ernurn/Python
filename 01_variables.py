#Variables in Python
# Exercises Level 1

first_name = 'Ernesto'
last_name = 'Nurnberg'
full_name = (first_name, last_name)
country = 'Argentina'
city = 'Eldorado'
age = 38
year = 2024
is_married = True
is_true = True
is_light_on = True
day, month = 25, 10
skills = ['Windows', 'Linux', 'Networking', 'Docker', 'AWS', 'Python']
person_info = {
    'first name' : 'Ernesto', 
    'last name' : 'Nurnberg',
    'country' : 'Argentina',
    'city' : 'Eldorado'
     }


print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print(full_name)
print('Country:', country)
print('City:', city)
print('Age:', age)
print('year', year)
print('Married:', is_married)
print('Is true', is_true)
print('Is light on', is_light_on)
print('Day', day, 'Month', month)
print('Skills:', skills)
print('Personal information', person_info)
print('\n')


# Different python data types

first_name = 'Ernesto'     # str
last_name = 'Nurnberg'       # str
country = 'Argentina'         # str
city= 'Eldorado'            # str
age = 38                   # int

#Exercises Level 2
# Printing out types

print(type('Ernesto'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Asabeneh'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip

# int to float

num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int

gravity = 9.81
print(int(gravity))             # 9

# int to str

num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float

num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list

first_name = 'Ernesto'
print(first_name)               # 'Ernesto'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['E', 'r', 'n', 'e', 's', 't', 'o']

# Using len()

print(len(first_name))
print(len(first_name,), len(last_name))

# operators

num_one = 5
num_two = 4

add = num_one + num_two
print(add)

subtract = num_two - num_one
print(subtract)

multiply = num_two * num_one
print(multiply)

divide = num_one / num_two
print(divide)

modulus = num_two % num_one
print(modulus)

power = num_one ** num_two
print(power)

floordiv = num_one // num_two
print(floordiv)

#Calculos con circulos
rad = 30
area_of_circle = 3.14 * rad ** 2
print('Area', area_of_circle)

circum_of_circle = 3.14 * (30 * 2)
print('Circunference', circum_of_circle)

radius = int(input('Enter the raidus:'))
area_of_circle = 3.14 * radius ** 2
print('Area', area_of_circle)

# Assign with inputs

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Entre your Country: ')
age = input('Enter your age: ')
print('First name:', first_name,'\t','Last name:', last_name, '\t', 'Country:', country, '\t','Age:',age)


