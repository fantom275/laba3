n = int(input("Enter number of days: "))

min_temp = int(input("Enter temperature: "))

for i in range(n - 1):
    t = int(input("Enter temperature: "))
    if t < min_temp:
        min_temp = t

print(min_temp)

if min_temp < -15:
    print("Yes")
else:
    print("No")
