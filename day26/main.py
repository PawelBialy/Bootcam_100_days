# ### LIST COMPREHENSION
# ### new_list = [ new_item for item in name_list ]
# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers ]
#
# name = "Angela"
# new_list = [letter for letter in name]
#
# list2 = [range (1,5)]
# double_list = [ num for num in list2]
#
# list2 = range (1,5)
# double_list = [ num for num in list2]
#
# list2 = range (1,5)
# double_list = [ num * 2 for num in list2]
#
# double_list = [ num * 2 for num in range (1,5)]
# double_list2= [ num * 2 for num in range (1,5)]
#
# ### List comprehension with test
# ### new_list = [ new_item for item in name_list if test ]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor","Freddie"]
# short_names = [name for name in names if len(name) < 4 ]
#
#
# short_names = [name for name in names if len(name) < 5 ]
# upper_case = [ name.upper() for name in names if len(name)> 5]
#
#
#numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#squared_numbers = [num * num  for num in numbers]

#numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#result = [num for num in numbers if num % 2 == 0 ]
# ### ALL DONE IN PYTHON CONSOLE
with open("file1.txt") as file1 :
    data_1_file = file1.readlines()

with open("file2.txt") as file2:
    data_2_file = file2.readlines()

result = [ int(num) for num in data_1_file if num in data_2_file]
print(result)