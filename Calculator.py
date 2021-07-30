import math

a = float(input("first num is:"))

op = input("Choose your operation from list above:\n1)+\n2)-\n3)*\n4)/\n5)sin\n6)cos\n7)tan\n8)radical\n9)factorial\n-please write the number of your opration:")

if op == ("1"):
    b = float(input("second num is: "))
    print("your result is :", (a + b))
if op == ("2"):
    b = float(input("second num is: "))
    print("your result is :", (a - b))
if op == ("3"):
    b = float(input("second num is: "))
    print("your result is :", (a * b))
if op == ("4"):
    b = float(input("second num is: "))
    if a != 0:
        print("your result is :", (a / b))
    if a == 0:
        print("Error! Zero Can't be divided")

if op == ("5"):
    print("your result is:",math.sin(a))
if op == ("6"):
    print("your result is:",math.cos(a))
if op == ("7"):
    print("your result is:",math.tan(a))
if op == ("8"):
    print("your result is:",math.sqrt(a))
if op == ("9"):
    print("your result is:",math.factorial(a))

