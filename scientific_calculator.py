#lets start import the module

import math

#scientific calculator

class calc(object):
    def add(num1, num2):
        answer = num1 + num2
        print("Sum = ", answer)
    
    def sub(num1, num2):
        answer = num1 - num2
        print("Difference = ", answer)

    def mul(num1, num2):
        answer = num1 * num2
        print("Multiplication = ", answer)

    def div(num1, num2):
        answer = num1 / num2
        print("Division = ", answer)

    def sinrad(num):
        answer = math.sin(num)
        print("Sine (%f) =%f" %(num, answer))

    def cosrad(num):
        answer = math.cos(num)
        print("Cosine (%f) =%f" %(num, answer))

    def tanrad(num):
        answer = math.tan(num)
        print("Tan (%f) =%f" %(num, answer))

    def cosecrad(num):
        answer = 1/(math.sin(num))
        print("Sine (%f) =%f" %(num, answer))

    def secrad(num):
        answer = 1/(math.cos(num))
        print("Sec (%f) =%f" %(num, answer))

    def cotrad(num):
        answer = 1/(math.tan(num))
        print("Cot (%f) =%f" %(num, answer))

    def sindeg(num):
        answer = 1/(math.sin(num))
        print("Sine (%f) =%f" %(num, answer))

print("Here the list of choice: ")
print("-" * 20)
print("1 : Addition \t\t  6 : Coisne in radians")
print("2 : Substraction \t  7 : Tan in radians")
print("3 : Multiplication \t  8 : Cosecant in radians")
print("4 : Division \t\t  9 : Secant in radians")
print("5 : Sine in radians \t  10 : Cot in radians")
print("-" * 20)

choice = ""
while True:
    try:
        print("If you want to exit-> press (e)")
        choice = input("Enter a number of choice: ")

    except:
        print ("Enter a valid number: ")

    if choice == '1':
        n1 = float(input("Enter the first number to add: "))
        n2 = float(input("Enter the second number to add: "))
        calc.add(n1, n2)

    elif choice == '2':
        n1 = float(input("Enter the first number to substract: "))
        n2 = float(input("Enter the second number to substract: "))
        calc.sub(n1, n2)

    elif choice == '3':
        n1 = float(input("Enter the first number to  multiplication: "))
        n2 = float(input("Enter the second number to  multiplication: "))
        calc.mul(n1, n2)

    elif choice == '4':
        n1 = float(input("Enter the first number to division: "))
        n2 = float(input("Enter the second number to division: "))
        calc.div(n1, n2)

    elif choice == '5':
        n = float(input("Enter a number to find its Sine in radians: "))
        calc.sinrad(n)

    elif choice == '6':
        n = float(input("Enter a number to find its Cosine in radians: "))
        calc.cosrad(n)

    elif choice == '7':
        n = float(input("Enter a number to find its Tan in radians: "))
        calc.tanrad(n)

    elif choice == '8':
        n = float(input("Enter a number to find its Cosecant in radians: "))
        calc.cosecrad(n)

    elif choice == '9':
        n = float(input("Enter a number to find its Secant in radians: "))
        calc.secrad(n)

    elif choice == '10':
        n = float(input("Enter a number to find its Cot in radians: "))
        calc.cotrad(n)

    elif choice == "e":
        break

    else:
        print("WARNING! Please enter a valid input")
