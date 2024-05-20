import math

print("ax^2 + bx + c = 0 の係数a, b, cを入力してください")
print("aは？")
a = int(input())
print("bは？")
b = int(input())
print("cは？")
c = int(input())

if a == 0:
    if a==0 and b==0:
        print("係数がおかしい")
    else:
        x = -c / b
        print("解は%f" %x )
else:
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("解は2つあり，x1=",  x1, ", x2=", x2)
    elif D == 0:
        x = (-b)/2
        print("解は重解となり，x=", x)
    else:
        print("解は虚数解となり，実数解は存在しない")