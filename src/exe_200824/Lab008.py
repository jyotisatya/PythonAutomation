#Write a program that classifies a triangle based on its side lengths. Given three input values representing the
# lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are
# equal), or scalene (no sides are equal). Use an if-else statement to classify the triangle.

l1 = int(input("Enter the length1"))
l2 = int(input('Enter the length2'))
l3= int(input("Enter the length3"))
if (l1 == l2 ==l3):
    print("Triangle is equilateral")
elif (l1==l2)or (l1==l3) or (l2==l3):
    print("Triangle is isoceles")
else:
    print("scalene")





