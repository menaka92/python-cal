past_calculations = []


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    try:
        return a/b
    except Exception as e:
        print(e)


def power(a, b):
    return a**b


def reminder(a, b):
    return a % b


def history():
    if past_calculations:
        for index, calc in enumerate(past_calculations):
            print(calc)
    else:
        print("No past calculations to show")
        return 0


def select_op(choice):
    if (choice == "?"):
        return history()
    if (choice == "#"):
        return -1
    elif (choice in ('+', '-', '*', '/', '%')):
        while (True):
            num1s = str(input("enter first number: "))
            print(num1s)
            if num1s.endswith('$'):
                return 0
            if num1s.endswith('#'):
                return -1

            try:
                num1 = float(num1s)
                break
            except:
                print("not a valid number,please enter again")
                continue

        while (True):
            num2s = str(input("Enter second number: "))
            print(num2s)
            if num2s.endswith('$'):
                return 0
            if num2s.endswith('#'):
                return -1
            try:
                num2 = float(num2s)
                break
            except:
                print("not a valid number , please enter again")
                continue

    result = 0.0
    last_calculation = ""
    if choice == '+':
        result = add(num1, num2)
    elif choice == '-':
        result = sub(num1, num2)
    elif choice == '*':
        result = mul(num1, num2)
    elif choice == '/':
        result = div(num1, num2)
    elif choice == '^':
        result = power(num1, num2)
    elif choice == '%':
        result = reminder(num1, num2)
    else:
        print("something went wrong")

    last_calculation = "{0} {1} {2} = {3}".format(num1, choice, num2, result)
    print(last_calculation)
    past_calculations.append(last_calculation)


while True:
    print("Select operation.")
    print("1.Add: + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide : / ")
    print("5.Power: ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset: $ ")

    choice = input("Enter choice ('+', '-', '*', '/', '%'): ")
    print(choice)

    if select_op(choice) == -1:
        print("done. terminating")
       

