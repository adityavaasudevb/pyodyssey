def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# print(operations["*"](4,8))
import art

def calculator():
    print(art.logo)
    num1 = int(input("What's the first number?:"))
    flag = True
    while(flag):

        for op in operations:
            print(op)
        op = input("Pick an operation:")

        num2 = int(input("What's the next number?"))
        res = operations[op](num1,num2)
        print(f"{num1} {op} {num2} = {res}")

        choice=input("Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation:")
        if choice=="y":
            num1=res
        else:
            flag = False
            print("\n" * 20)
            calculator()

calculator()


