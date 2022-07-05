x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15;

# 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]["last_name"] = "Bryant"

# 3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"



# -----------------------------# 

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# 2.
# def iterateDictionary(some_list):
#     for dictionary in some_list:
#         for key in dictionary.keys():
#             print(key + " - " + dictionary[key])


# iterateDictionary(students) 


# 3. 
# def iterateDictionary2(key_name, some_list):
#     for dictionary in some_list:
#         for key in dictionary.keys():
#             if key == key_name:
#                 print(dictionary[key_name])

# iterateDictionary2('last_name', students)


# -------------------------- #
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(str(len(some_dict[key])) + " " + key.upper())
        for value in some_dict[key]:
            print(value)
        print()
printInfo(dojo)

