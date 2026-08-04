# # Day 3: 30 Days of Python Programming
# import math
#
# age = 30
# height = 5.11
# complex_num = 3 + 4j
#
# # 4. Area of a Triangle
# base = int(input("Enter base: "))
# height = int(input("Enter height: "))
# area = 0.5 * base * height
# print("The area of the triangle is", int(area))
#
# # 5. Perimeter of a Triangle
# side_a = int(input("Enter side a: "))
# side_b = int(input("Enter side b: "))
# side_c = int(input("Enter side c: "))
# perimeter = side_a + side_b + side_c
# print("The perimeter of the triangle is", int(perimeter))
#
# # 6. Area and Perimeter of a Rectangle
# length = int(input("Enter length: "))
# width = int(input("Enter width: "))
# area = length * width
# perimeter = 2 * (length + width)
# print("The area of the rectangle is", int(area))
# print("The perimeter of the rectangle is", int(perimeter))
#
# # 7. Radius and Circumference of a Circle
# radius = int(input("Enter radius: "))
# area = math.pi * radius ** 2
# circumference = 2 * math.pi * radius
# print("The area of the circle is", round(area, 2))
# print("The circumference of the circle is", round(circumference, 2))
#
# # 8. Slope of y = 2x - 2
# # mx+b
# m = 2
# x = 0
# b = -2
# y = 0
# x_intercept = -b / m
# y_intercept = 2 * x - 2
# print("The x- intercept of y = 2x - 2 =", int(x_intercept))
# print("The y-intercept of y = 2x- 2 =", int(y_intercept))

# 12. Find the lenth of python and dragon and make a falsy comparison
print(len('python') != len('dragon'))

# 13. Find if 'on' is in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 14. Use in operator to check if jargon is in the sentence
print('jargon' in 'I hope this course is not full of jargon.')

# 15. There is no 'on' in both dragon and python
print('on' in ['python', 'dragon'])

# 16. Find the length of 'python', convert it to a float, then convert it to a string
python_length = len('python')
python_float = float(python_length)
python_string = str(python_float)
print(python_string)

# 17. How to check if a number is even or not using python?
even_num = 2
odd_num = 3
print('To check for an even number, use the modulo operator %')
print('2 is even because 2 % 2 == 0')
print(even_num % 2 == 0)
print('3 is odd because 3 % 2 != 0')
print(odd_num % 2 == 0)

# 18. Check if the floor division of 7 by 3 == int value of 2.7
floor_div = 7 // 3
print(floor_div == int(2.7))

# 19. Check if '10' is equal to type 10
print('10' == 10)

# 20. Check if int('9.8') == 10
# print(int('9.8') == 10) // invalid 9.8 is a float not an int

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay per hour.
def pay_per_hour():
    hours = int(input("Enter hours: "))
    rate = float(input("Enter rate per hour: "))
    return hours * rate

print('Your weekly earnings is', pay_per_hour())
