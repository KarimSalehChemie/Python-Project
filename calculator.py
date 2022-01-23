#calculator

from random import choice

while True:
    print("Choose a calculator: ")
    print("1. Simple calcluator.")
    print("2. Advance calcluator.")
    print("3. Scientific calcluator.")
    print("e. Exit")
    
    while True:
        choice = input ("Select a calculator [1], [2], [3], or [e]: ")
        if choice in ("1", "2", "3", "e"):
            break
        else:
            print("Invalid Input")

    if choice == "1":
        exec (open("simple_calculator.py").read())
    
    elif choice == "2":
        exec (open("advanced_calculator.py").read())

    elif choice == "3":
        exec (open("scientific_calculator.py").read())

    elif choice == "e":
        break

