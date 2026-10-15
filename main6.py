a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

for n in [a, b, c]:
    n = abs(n)
    s = 0

    while n > 0:
        s += n % 10
        n //= 10

    print(s)
