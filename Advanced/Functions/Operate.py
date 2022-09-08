def operate(operation, *args):
    def add(*args):
        return sum(args)

    def subtract(x, *args):
        return x + sum(-y for y in args)

    def multiply(*args):
        v = 1
        for i in args:
            v *= i
        return v

    def devide(x, *args):
        result = x
        for value in args:
            result /= value
        return result

    if operation == '+':
        return add(*args)
    elif operation == '-':
        return subtract(*args)
    elif operation == '*':
        return multiply(*args)
    elif operation == '/':
        return devide(*args)

print(operate("-", 1, 2, 3))