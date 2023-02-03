### LIST COMPREHENSION
### new_list = [ new_item for item in name_list ]
numbers = [1,2,3]
new_numbers = [n+1 for n in numbers ]

name = "Angela"
new_list = [letter for letter in name]

list2 = [range (1,5)]
double_list = [ num for num in list2]

list2 = range (1,5)
double_list = [ num for num in list2]

list2 = range (1,5)
double_list = [ num * 2 for num in list2]

double_list = [ num * 2 for num in range (1,5)]
double_list2= [ num * 2 for num in range (1,5)]

### List comprehension with test
### new_list = [ new_item for item in name_list if test ]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor","Freddie"]
short_names = [name for name in names if len(name) < 4 ]


short_names = [name for name in names if len(name) < 5 ]
upper_case = [ name.upper() for name in names if len(name)> 5]



### ALL DONE IN PYTHON CONSOLE