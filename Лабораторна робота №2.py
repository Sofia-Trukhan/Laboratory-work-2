import math
x = float(input("Введіть значення x: "))
if x <=0:
    print("Помилка: x має бути більше 0")
else:
    y = (math.sin(x)**3 - math.cos(x-1)**2)/(math.atan(x+1)+(math.log10(x))**(1/3))
    print("y = ", y)

