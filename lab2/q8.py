while True:  
    operator = input("Enter operator: ")

    if operator == "+":
        print(f"{num1} + {num2} = {num1+num2}")
    elif operator == "-":
        print(f"{num1} - {num2} = {num1-num2}")
    elif operator == "*":
        print(f"{num1} * {num2} = {num1*num2}")
    elif operator == "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1/num2}")
        else:
            print("Division by zero is undefined")
    elif operator == "%":
        if num2 != 0:
            print(f"{num1} % {num2} = {num1%num2}")
        else:
            print("Modulus by zero is undefined")
    elif operator == "exit":
        print("Exiting the code")
        break
    else:
        print("Enter a valid operator")
        
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
        