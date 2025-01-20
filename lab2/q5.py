def fact(n):
    if n <0:
        return "Not defined"
    elif n ==0:
        return 1
    else:
        result = 1
        for i in range (1,n+1):
            result = result*i
        return result

num = int(input("Enter a number: "))
factorial = fact(num)
print(f"Factorial of {num} is {factorial}")