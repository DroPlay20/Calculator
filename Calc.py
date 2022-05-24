# CALCULATOR BY DRO20
#
# Hello, this is a project from Dro20 called Calculator
# Documentation of my project: https://github.com/DroPlay20/Calculator
import mymath
import time

time.sleep(0.2)
print("Command:")


print(" ")
time.sleep(0.2)

while True:
    for i in range(24):
        print("")
        print("Command:")
    print("-1 - exit from the program")
    print("0 - About the project")
    print("1 - Plus")
    print("2 - Minus")
    print("3 - Division")
    print("4 - Multiplication")
    print("5 - Remainder of the division")
    print("6 - Degree")
    print("7 - Number of digits in a number")
    print("8 - The sum of the digits in a number")
    print("9 - Logarithm")
    print("10 - Radical")
    print("11 - Random number")
    print("12 - Find a number by percentage")
    print("13 - Find percentage of a number")
    com = str(input("Print command "))
    if com == "-1":
        for i in range(24):
            print("")
        print("Bye")
        quit()
    if com == "0":
        print("Hello, this is a project calculator from Dro20")
        time.sleep(1)
        print("I created this project for myself so that it would be easier for me to program and")
        print("solve problems with large numbers")
        time.sleep(1)
        print("I will be glad if you support me and give me some money https://www.donationalerts.com/r/dro_play")
        time.sleep(1)
        print("how my program works is written here - https://github.com/DroPlay20/Calculator")
    if com == "1":
        print("write 2 numbers through enter")
        print(mymath.Plus(int(input()), int(input())))
    if com == "2":
        print("write 2 numbers through enter")
        print(mymath.Minus(int(input()), int(input())))
    if com == "3":
        print("write 2 numbers through enter")
        print(mymath.Div(int(input()), int(input())))
    if com == "4":
        print("write 2 numbers through enter")
        print(mymath.Mul(int(input()), int(input())))
    if com == "5":
        print("write 2 numbers through enter")
        print(mymath.OOD(int(input()), int(input())))
    if com == "6":
        print("write 2 numbers through enter")
        print(mymath.STEP(int(input()), int(input())))
    if com == "7":
        print("write 1 number")
        print(mymath.WMN(str(input())))
    if com == "8":
        print("write 1 number")
        print(mymath.SUMN(int(input())))
    if com == "9":
        print("write 1 number")
        print(mymath.LOG(int(input())))
    if com == "10":
        print("write 1 number")
        print(mymath.KOR(int(input())))
    if com == "11":
        print("write 1 min number and write 1 max number")
        print(mymath.RAND(int(input()), int(input())))
    if com == "12":
        print("write 2 numbers through enter")
        print("The first number is a number, the second number is the percentage to be found")
        print(mymath.FPN(int(input()), int(input())))
    if com == "13":
        print("write 2 numbers through enter")
        print("The first number is a number, the second number is the percentage of which is equal to the number")
        print(mymath.FNP(int(input()), int(input())))