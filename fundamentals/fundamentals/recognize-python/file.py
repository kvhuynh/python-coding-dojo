num1 = 42 #variable declaration, intialize int
num2 = 2.3 #variable declaration, intialize int
boolean = True #variable declaration, intialize bool
string = 'Hello World' #variable declaration, intialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, intialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, intialize dict
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, intialize tuple
print(type(fruit)) # log statement, type
print(pizza_toppings[1]) # log statement, value in list
pizza_toppings.append('Mushrooms') # list statement, add element
print(person['name']) # log statement, print value at dictionary key
person['name'] = 'George' # dict, change value
person['eye_color'] = 'blue' # dict, change value
print(fruit[2]) # log statement, value at list index 2

if num1 > 45: # conditional, if var > 45
    print("It's greater") # log statement, string
else: # conditional, else
    print("It's lower") # log statement, string

if len(string) < 5: # conditional, if length of string is < 5
    print("It's a short word!") # log statement, string
elif len(string) > 15: # conditional elif length of string > 15
    print("It's a long word!") # log statement, string
else: # conditional else
    print("Just right!") # log statement, string

for x in range(5): # for loop start = 0, stop = 4
    print(x) # log statement int
for x in range(2,5): # for loop start = 2 stop = 4 
    print(x) # log statement int
for x in range(2,10,3): # for loop start = 2 stop = 9, step = 3 
    print(x) # log statement int
x = 0 # variable declaration, int
while(x < 5): # while loop while x <5
    print(x) # log statement int
    x += 1 # increment x

pizza_toppings.pop() # list delete  lastvalue
pizza_toppings.pop(1) # list delete value at index 1

print(person) # log statement
person.pop('eye_color') # dict remove key and value
print(person) # log statement

for topping in pizza_toppings: # for each loop
    if topping == 'Pepperoni': # if statement
        continue # continue
    print('After 1st if statement') # log 
    if topping == 'Olives': # if statement
        break # break

def print_hello_ten_times(): # defining function 0 prameters
    for num in range(10): # for loop from 0 to 9
        print('Hello') # log statement

print_hello_ten_times() # run function

def print_hello_x_times(x): # defining function 1 parameter x
    for num in range(x): # for loop for each num in x
        print('Hello') # log statement

print_hello_x_times(4) # run function

def print_hello_x_or_ten_times(x = 10): # defining function 1 paramenterx  
    for num in range(x): # for loop for each number in range (10)
        print('Hello') # log statement

print_hello_x_or_ten_times() # run function with 0 arguments
print_hello_x_or_ten_times(4) # run function with 1 argument


"""
Bonus section
"""

# print(num3) # name error
# num3 = 72
# fruit[0] = 'cranberry' # type error
# print(person['favorite_team']) # key error
# print(pizza_toppings[7]) # name error
# print(boolean) # name error
# fruit.append('raspberry') # atrtribute error
# fruit.pop(1) # attribute error