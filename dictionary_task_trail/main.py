list_1 = [ "ball", "baseball", "conditioner" ]
list_2 = ["chocolate", "sweet_drinks", "bars" ]
list_3 = ["toothpaste , shower_gel, razor" ]

poland = ["Kraków, Wrocław, Warszawa, Rzeszów" ]
holland = [ "Amsterdam, Rotterdam, Breda"]
czech = [ "Praga, Zlin, Brno"]

all_departmets = [ "sports department, food department, cosmetics department"]
sports_department = {
        "number_of_racks1": 3,
        "number_of_shelves1": 18,
        "elements1" : list_1,
    }

food_department = {
        "number_of_racks2": 6,
        "number_of_shelves2": 36,
        "elements2": list_2,
    }

cosmetics_department = {
        "number_of_racks3" :  7,
        "number_of_shelves3" : 24,
        "elements3" : list_3,
    }

store = {
        "size" : "middle",
        "department" : [sports_department, food_department, cosmetics_department],
        "cities" : [poland, holland, czech],
    }


for elem in store['cities'][0]:
   print( "In Poland stores are in sample cities : " + elem , )
for elem1 in all_departmets:
    print ("In this stores are departments of :  " + elem1 )
for elem3 in cosmetics_department['elements3']:
 print ( "In sports department are " +  str(cosmetics_department['number_of_racks3'] ) + ' racks and ', str(cosmetics_department["number_of_shelves3"] )  + ' shelves. Products that are on the shelves are : ' + elem3,'.'  )



#print("This store chain are + str(len(store['department'][0])) + size" )


    # for elem in store["citis"][0]["department"]:
    # print(elem)