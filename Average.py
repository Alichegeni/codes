n = input("please write your full name: ")
a = float(input("please enter your first course point: "))
b = float(input("please enter your second course point: "))
c = float(input("please enter your third course point: "))

average = (a + b + c) / 3


if average >= 17:
    print("your average is", average,"and that's great")
elif  17 > average >= 12 :
    print("your average is", average,"and it's normal")
elif average < 12 : 
    print("your average is", average,"and you fail!")

