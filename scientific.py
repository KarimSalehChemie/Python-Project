import math


class scientific:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # This function adds two numbers
    def add(self):
        return self.x + self.y

    # This function subtracts two numbers
    def sub(self):
        return self.x - self.y

    # This function multiplies two numbers
    def multi(self):
        return self.x * self.y

    # This function divides two numbers
    def div(self):
        return self.x / self.y

    # This function gives the exponent power of a number
    def exponent(self):
        return self.x ** self.y

    # This function gives the log of a number
    def log(self):
        return math.log(int(self.x))

    # Operation Type
    def decision(self, operator):
        if operator == '+':
            return self.add()
        elif operator == '_':
            return self.sub()
        elif operator == '*':
            return self.multi()
        elif operator == '/':
            return self.div()
        elif operator == '^':
            return self.exponent()


class new_scientific:
    def __init__(self, x):
        self.x = x

    # This function gives the log of a number
    def cos(self):
        return math.cos(int(self.x))

    # This function gives the log of a number
    def sin(self):
        return math.sin(int(self.x))

    # This function gives the log of a number
    def tan(self):
        return math.tan(int(self.x))

    # This function gives the log of a number
    def log(self):
        return math.log(int(self.x))

    # This function gives the log of a number
    def fact(self):
        return math.factorial(int(self.x))

    def str_decision(self, str_operator):
        if str_operator == 'cos':
            return self.cos()
        if str_operator == 'sin':
            return self.sin()
        if str_operator == 'tan':
            return self.tan()
        if str_operator == 'log':
            return self.log()
        if str_operator == '!':
            return self.fact()
