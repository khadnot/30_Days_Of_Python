# Day 3: 30 Days of Python Programming
import math

age = 30
height = 5.11
complex_num = 3 + 4j

# 4. Area of a Triangle
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is", int(area))

# 5. Perimeter of a Triangle
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is", int(perimeter))

# 6. Area and Perimeter of a Rectangle
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is", int(area))
print("The perimeter of the rectangle is", int(perimeter))

# 7. Radius and Circumference of a Circle
radius = int(input("Enter radius: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print("The area of the circle is", round(area, 2))
print("The circumference of the circle is", round(circumference, 2))

# 8. Slope of y = 2x - 2
# mx+b
m = 2
x = 0
b = -2
y = 0
x_intercept = -b / m
y_intercept = 2 * x - 2
print("The x- intercept of y = 2x - 2 =", int(x_intercept))
print("The y-intercept of y = 2x- 2 =", int(y_intercept))
