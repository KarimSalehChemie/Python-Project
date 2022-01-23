#lets start import the module

import math

#advanced calculator

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def decision(self, user_decision):
        if user_decision == "+":
            return self.add()
        elif user_decision == "-":
            return self.subtract()
        elif user_decision == "*":
            return self.multiply()
        elif user_decision == "/":
            return self.divide()

while True:
    print("WARNING! Please enter a space in between")
    user_input = input("Please enter a calculation: ")
    user_input = user_input.strip().split(" ")

    user_num1 = int(user_input[0])
    user_num2 = int(user_input[2])
    decision = user_input[1]

    calc = Calculator(user_num1, user_num2)
    result = calc.decision(decision)
    print(result)

    further_calculation = input("Do you want to make any further calculation (y or n)?: ")

    if further_calculation.lower()[0] == "y":
        continue
    elif further_calculation.lower()[0] == "n":
        break
    else:
        print("Invalid Input")
