a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

while y != 0:
    x, y = y, x % y

nsd = x
nsk = a * b // nsd

print("nsk =", nsk)
