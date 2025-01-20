def is_prime(n):
    if num <=1:
        return False
    else:
        c=2
        while(c*c<=n):
            if n%c ==0:
                return False
            c = c+1
        if c*c>n:
            return True
    return False
num = int(input("Enter a number: "))
ans = is_prime(num)
print(f"{num} is {ans}")

    