a = input("what is your first side length: ")
b = input("what is your second side length: ")
c = input("what is your third side length: ")

if a + b > c : 
    if a + c > b:
        if b + c > a:
            print("this triangle exist!")
else:
    print("this triangle does't exist!")
