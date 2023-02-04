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
# with open("file1.txt") as file1 :
#     data_1_file = file1.readlines()
#
# with open("file2.txt") as file2:
#     data_2_file = file2.readlines()
#
# result = [ int(num) for num in data_1_file if num in data_2_file]
# print(result)
#
# ### Dict comprehentions
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor","Freddie"]
# import random
# students_score = {student:random.randindt(0,100) for student in names}


# import random
# students_scores = {student:random.randint(0,100) for student in names}
# passed_students = {student:score for (student,score) in students_scores.items() if score >= 50 }


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day:(temp * 9/5 ) + 32 for (day,temp) in weather_c.items()}


### LOOPING THROUGH DICTIONARIES:
student_dict ={
    "student":["Angela", "Paul", "James"],
    "score":[62,29,88]
}
# for (key, value) in student_dict.items():
#     print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
###Loop through rows of a data frame :

for (intex, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
