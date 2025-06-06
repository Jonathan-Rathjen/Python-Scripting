side1 = int(input("Please input the length of the first side of your triangle: "))
side2 = int(input("Please input the length of the second side of your triangle: "))
side3 = int(input("Please input the length of the third side of your triangle: "))

if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    print("Those lengths are not possible to form a triangle")
    quit()
elif side1 == side2 and side2 == side3:
    print("That is an Equalateral Triangle!")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("That is an Isosceles Triangle!")
else:
    print("That is a Scalene Triangle!")