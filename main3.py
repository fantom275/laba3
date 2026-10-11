n = int(input("Enter a number: "))
maximum = n 

while n != 0:
    if n > maximum:
        maximum = n
    n = int(input("Enter a number: "))

print(maximum)