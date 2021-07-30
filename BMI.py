w = int(input("please insert your weight in kilogram: "))
h = int(input("please insert your height in centimeter:"))
H = ((h/100)**2)
 
BMI = (w / H)
if w == 0: 
    print("you can not be zero kg! please enter your weight correctly")
if w != 0:
    if BMI < 18.5:
        print("your BMI is:", BMI, "you are underweight")
    if 18.5 <= BMI < 25:
        print("your BMI is:", BMI, "and you are normal")
    if 25 <= BMI < 30:
        print("your BMI is:", BMI, "and you are overweight, please be careful")
    if 30 < BMI < 35:
        print("your BMI is:", BMI, "and you are overweight, start workout ASAP")
    if 35 <= BMI :
        print("your BMI is:", BMI, "and you are overweight, it's better to call a health consultor")