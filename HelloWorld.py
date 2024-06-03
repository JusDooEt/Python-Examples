from classes import Person


# Declaring Variables
age = 20                # int
price = 19.95           # float
first_name = "Cameron"  # string
is_online = True        # boolean
dave = Person("David", "Matthews", 34, True) # Person class object

# Prints to console like cout
print(age)

# input() function prints a prompt and returns the console input
#first_name = input("What is your name? ")
print ("Hello " + first_name)

#birth_year = input("Enter your birth year: ")

# Type conversion
#age = 2024 - int(birth_year)
#print("Age = " + str(age))

# String methods
course = 'Python for Beginners'
index = course.find('for')        # This function will 'find' a 'y' character and return the index of that character in the string (index = 7)
print(course.upper())             # This function will return the course string in upper case
print(course.replace('for', '4')) # This function will find 'for' and replace it with '4'
print('Python' in course)         # This returns a boolean value if 'Python' is found in the string course

# Operators
print(10 / 3)                   # One '/' will return a float type value
print(10 // 3)                  # Two '/' will return an integer type value truncating the decimal
print(10 ** 3)                  # exponent operator (10^3)

x = 10

# This does same thing as in c++
x = x + 3   
x += 3

# Logical Operators
price = 25
print(price > 10 and price < 30)    # The same as && in c++
print(price > 10 or price < 30)     # The same as || in c++
print(not price > 10)               # The same as ! in c++

# if Statements
temperature = 35

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:              # 'elif' == 'else if' in c++
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("done")


# While loops
i = 1
while i <= 10:                  # 1_000 = 1,000, 1_000_000 = 1,000,000, etc.
    print(i * '*')              # This will print '*' i amount of times
    i = i + 1
    
# Lists
names = ['Eric', 'Bean', 'Josh', 'Carly', 'Gerald']    
print(names)
print(names[0])         # Prints 'Eric'
print(names[-1])        # Prints 'Josh'
names[0] = 'Chloe'
print(names)

print(names[0:3])       # Prints the list from range [0, 3)

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
numbers.insert(2, 2.5)  # inserts 2.5 at index 2
print(numbers)
print(1 in numbers)     # Checks to see if 1 is in the list numbers. returns a boolean value
print(len(numbers))     # Returns the number of elements(n) in the list

for item in numbers:
    print(item)
    
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
    
# Range Function
numbers = range(5)          # this is equal to [0, 5)
print(numbers)
for x in numbers:
    print(x)
    
numbers = range(5, 10)      # this is equal to [5, 10)
print(numbers)
for x in numbers:
    print(x)
    
numbers = range(5, 10, 2)   # this is equal to [5, 10) with a step = 2 
print(numbers)
for x in numbers:
    print(x)
    
for number in range(5):     # Declaing the range in the for loop
    print(number)
    
# Tuples
numbers = (1, 2, 3, 3)          # Immutable/Unchangable (think const in c++)
numbers.count(3)                # Counts the amount of time 3 occurs in the tuple
numbers.index(3)                # Returns the index of the first instance of 3 in the tuple. This will return 2.

# Class examples
print(str(dave.first_name) + ' ' + str(dave.last_name))
print(str(dave.age))
print("Does " + dave.first_name + " like pizza?")

if bool(dave.likes_pizza):
    print("Yes!!! =)")
else:
    print("No... =(")    
    
print(str(dave.first_name) + ' is ')
dave.run()