#PRAGYA MISHRA 0801IT22158
def gcd(num1, num2):
    i = 1
    gcd = 1  
    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            gcd = i  
        i += 1  
    return gcd
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("The GCD of", a, "and", b, "is:", gcd(a,b))
