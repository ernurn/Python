### Lists ### 

my_list = list()
my_other_list = []

print(my_list) # []
print(len(my_list)) # 0

my_list = [35, 26, 28, 38]

print(my_list) # [35, 26, 28, 38]
print(len(my_list)) # 4
print(type(my_list)) # <class 'list'>

my_other_list = ['playa', 35, True, 1.73]
print(my_other_list) # 'playa', 35, True, 1.73]
print(len(my_other_list)) # 4
print(type(my_other_list)) # <class 'list'>

print(my_other_list[-2]) # True
print(my_other_list.count(35)) # 1

print(my_list + my_other_list) # [35, 26, 28, 38, 'playa', 35, True, 1.73]

my_other_list.append('West')
print(my_other_list) # ['playa', 35, True, 1.73, 'West']

my_other_list.insert(1,'networking')
print(my_other_list) # ['playa', 'networking', 35, True, 1.73, 'West']

print(my_other_list.pop()) #West
print(my_other_list) #['playa', 'networking', 35, True, 1.73]

print(my_other_list.pop(2)) # 35
print(my_other_list) # ['playa', 'networking', True, 1.73]

print(my_list) # [35, 26, 28, 38]
my_list.remove(28)
print(my_list) # 35, 26, 38]

print(my_list) # [35, 26, 38]
del my_list[0]
print(my_list) # [26, 38]

my_other_list.reverse()
print(my_other_list) # [1.73, True, 'networking', 'playa']

my_new_list = my_list.copy()
del my_list
print(my_new_list)

my_new_list.append(15)
print(my_new_list)
my_new_list.sort()
print(my_new_list)

