def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def main():
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }

    numb1 = int(input("What is the first number?: "))
    numb2 = int(input("What is the next number?: "))

    for key in operations:
        print(key)

    oper = input("Pick an operation?: ")
    result = operations[oper](numb1, numb2)

    print(f"{numb1} {oper} {numb2} = {result}")


if __name__ == "__main__":
    main()
