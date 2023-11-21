from art import logo

def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def calculator():
    print(logo)
    contnious="y"
    numb1 = float(input("What is the first number?: "))
    while contnious=="y":
        operations = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div,
        }

        numb2 = float(input("What is the next number?: "))

        for key in operations:
            print(key)

        oper = input("Pick an operation?: ")
        result = operations[oper](numb1, numb2)

        print(f"{numb1} {oper} {numb2} = {result}")

        contnious=str(input(f"Type 'y' to continue calculating with {result}, or 'n' to exit.: "))
        numb1=result
        if contnious=="n":
            calculator()

calculator()