# Day 2: 30 Days of Python Programming
import math

# Level 1
first_name = "Kenn"
last_name = "Hadnot"
full_name = first_name + " " + last_name
country = "United States"
city = "Los Angeles"
age = 23
is_married = True
is_true = False
is_light = True
hobby_1, hobby_2, hobby_3 = "music", "coding", "disc golf"
hobbies = [hobby_1, hobby_2, hobby_3]

# Level 2
print("Variable first_name is of type:", type(first_name))
print("Variable last_name is of type:", type(last_name))
print("Variable full_name is of type:", type(full_name))
print("Variable country is of type:", type(country))
print("Variable city is of type:", type(city))
print("Variable age is of type:", type(age))
print("Variable is_married is of type:", type(is_married))
print("Variable is_true is of type:", type(is_true))
print("Variable is_light is of type:", type(is_light))
print("Variable hobbies is of type:", type(hobbies))

print("The length of first_name is:", len(first_name))
print("The length of last_name is:", len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = round(math.pi * radius ** 2, 2)
print("The area of the circle is", area_of_circle, "meters")
circumference = round(2 * math.pi * radius, 2)
print("The circumference is", circumference, "meters")
new_radius = int(input("Enter a new radius: "))
new_area_of_circle = round(math.pi * new_radius ** 2, 2)
print("The new area of the circle is", new_area_of_circle, "meters")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))
print(first_name, last_name, "is from", country, "and is", age, "years old!")
