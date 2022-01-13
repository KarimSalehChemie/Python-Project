# Import the classes and functions from the main file
import simple as sp
import advanced as ad
import scientific as sc
import re

while True:
    # Select Calculator Type
    print("Select calculator type.")
    print('1.Basic')
    print('2.Advanced')
    print('3.Scientific')
    print('Or q.Quit')

    # take input from the user
    while True:
        choice = input('Enter your choice(1/2/3/q): ')
        if choice in ('1', '2', '3', 'q'):
            break
        else:
            print("Invalid Input")

    # Simple Calculator
    if choice == '1':
        while True:
            print('Basic Calculator')
            print('Select operation.')
            print('1.Addition')
            print('2.Subtraction')
            print('3.Multiplication')
            print('4.Division')

            # check if choice is one of the four options
            choice = input('Enter choice(1/2/3/4): ')

            # check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):

                while True:
                    x = input('Enter first number: ')
                    try:
                        x = float(x)
                        break
                    except ValueError:
                        print('not a number!')
                        continue

                while True:
                    y = input('Enter second number: ')
                    try:
                        y = float(y)
                        break
                    except ValueError:
                        print('not a number!')
                        continue

                obj = sp.simple(x, y)

                if choice == '1':
                    print(x, '+', y, '=', obj.add())

                elif choice == '2':
                    print(x, '-', y, '=', obj.sub())

                elif choice == '3':
                    print(x, '*', y, '=', obj.multi())

                elif choice == '4':
                    print(x, '/', y, '=', obj.div())

            else:
                print("Invalid Input")
                continue

                # check if user wants another calculation
                # break the while loop if answer is no
            quite = input('Do you want to quit this calculator? (y/n): ')
            if quite == 'y':
                break
            elif quite == 'n':
                continue
            else:
                print("Invalid Input")

    # Advanced Calculator
    if choice == '2':
        operator = ''
        print('Advanced Calculator')
        print('Equation Format: X operator Y')
        print('Addition +')
        print('Subtraction _')
        print('Multiplication *')
        print('Division /')

        calculation = input("Enter your equation: ")

        for i in calculation:
            if i == '+' or i == '_' or i == '*' or i == '/':
                operator = i.strip()

        num = re.findall(r'-?\d+\.?\d*', calculation)
        x = float(num[0])
        y = float(num[1])

        while True:

            if operator == '+':
                adv = ad.advanced(x, y)
                result = adv.decision(operator)
                print(x, operator, y, '=', result)

            if operator == '_':
                adv = ad.advanced(x, y)
                result = adv.decision(operator)
                print(x, operator, y, '=', result)

            if operator == '*':
                adv = ad.advanced(x, y)
                result = adv.decision(operator)
                print(x, operator, y, '=', result)

            if operator == '/':
                adv = ad.advanced(x, y)
                result = adv.decision(operator)
                print(x, operator, y, '=', result)

            # check if user wants another calculation
            # break the while loop if answer is no
            print('If you want to quit: Write(q)')
            next_step = input('Next Step: ')
            if next_step == 'q':
                break
            else:
                for i in next_step:
                    if i == '+' or i == '_' or i == '*' or i == '/':
                        operator = i.strip()

                num = re.findall(r'-?\d+\.?\d*', next_step)
                x = result
                y = float(num[0])

    # Scientific Calculator
    if choice == '3':
        operator = ''
        print('Scientific Calculator')
        print('Equation Format: X operator Y')
        print('Addition +       | Factorial!')
        print('Subtraction _    | sin')
        print('Multiplication * | cos')
        print('Division /       | tan')
        print('Exponent ^       | log')

        while True:
            print('If you want to quit: Write(q)')
            calculation = input("Enter your equation: ")
            if calculation == 'q':
                break

            for i in calculation:
                if i == '+' or i == '_' or i == '*' or i == '/' or i == '^' or i == '!':
                    operator = i.strip()

            str_operator = ''.join(re.split("[^a-zA-Z]*", calculation))
            num = re.findall(r'-?\d+\.?\d*', calculation)

            if str_operator == 'sin' or str_operator == 'cos' or str_operator == 'tan' \
                    or str_operator == 'log' or str_operator == '^' or operator == '!':

                x = float(num[0])
                if str_operator == 'cos':
                    sci = sc.new_scientific(x)
                    result = sci.str_decision(str_operator)
                    print(str_operator, x, '=', result)

                if str_operator == 'sin':
                    sci = sc.new_scientific(x)
                    result = sci.str_decision(str_operator)
                    print(str_operator, x, '=', result)

                if str_operator == 'tan':
                    sci = sc.new_scientific(x)
                    result = sci.str_decision(str_operator)
                    print(str_operator, x, '=', result)

                if str_operator == 'log':
                    sci = sc.new_scientific(x)
                    result = sci.str_decision(str_operator)
                    print(str_operator, x, '=', result)

                if operator == '!':
                    sci = sc.new_scientific(x)
                    result = sci.str_decision(operator)
                    print(str_operator, x, '=', result)

                quite = input('Do you want to quit this calculator? (y/n): ')
                if quite == 'y':
                    break
                elif quite == 'n':
                    continue
                else:
                    print("Invalid Input")

            if operator == '+' or operator == '_' or operator == '*' or operator == '/' or operator == '^':

                x = float(num[0])
                y = float(num[1])

                while True:
                    if operator == '+':
                        sci = sc.scientific(x, y)
                        result = sci.decision(operator)
                        print(x, operator, y, '=', result)

                    if operator == '_':
                        sci = sc.scientific(x, y)
                        result = sci.decision(operator)
                        print(x, operator, y, '=', result)

                    if operator == '*':
                        sci = sc.scientific(x, y)
                        result = sci.decision(operator)
                        print(x, operator, y, '=', result)

                    if operator == '/':
                        sci = sc.scientific(x, y)
                        result = sci.decision(operator)
                        print(x, operator, y, '=', result)

                    if operator == '^':
                        sci = sc.scientific(x, y)
                        result = sci.decision(operator)
                        print(x, operator, y, '=', result)

                    # check if user wants another calculation
                    # break the while loop if answer is no
                    print('If you want to quit: Write(q)')
                    next_step = input('Next Step: ')
                    if next_step == 'q':
                        break
                    else:
                        for f in next_step:
                            if f == '+' or f == '_' or f == '*' or f == '/':
                                operator = f.strip()
                        x = result
                        num = re.findall(r'-?\d+\.?\d*', next_step)
                        y = float(num[0])

    if choice == 'q':
        break
