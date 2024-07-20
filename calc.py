import math


def summa(first, second):
    return first + second


def sub(first, second):
    return first - second


def mult(first, second):
    return first * second


def dev(first, second):
    return first / second


def calc(first, second, oper):
    result = None
    if oper == '+':
        result = summa(first, second)
    elif oper == '-':
        result = sub(first, second)
    elif oper == '*':
        result = mult(first, second)
    elif oper == '/':
        if second == 0:
            print('It is forbidden to divide by zero')
            return None
        result = dev(first, second)
    elif oper == '**':
        result = first ** second
    elif oper == 'log':
        if first <= 0 or second <= 0:
            print('Logarithm base and argument must be positive numbers')
            return None
        result = math.log(first, second)
    else:
        print('Incorrect operation')
        return None
    return result


def operation():
    mes = input('Choose operation (Enter +, -, *, /, **, log): ')
    correct_operation = ['+', '-', '/', '*', '**', 'log']
    while mes not in correct_operation:
        print('This operation is not listed. Try again.')
        mes = input('Choose operation (Enter +, -, *, /, **, log): ')
    return mes


def run():
    while True:
        try:
            first = float(input('Enter first number: '))
        except ValueError:
            print('You have entered incorrect data. Please enter a number.')
            continue

        try:
            second = float(input('Enter second number: '))
        except ValueError:
            print('You have entered incorrect data. Please enter a number.')
            continue

        op = operation()
        result = calc(first, second, op)
        if result is not None:
            print(f'Result: {result}')

        answer = input('Would you like to continue? (yes/no): ')
        if answer.lower() != 'yes':
            break


run()
