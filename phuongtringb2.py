import math
a=float(input("Nhập hệ số a:"))
b=float(input("Nhập hệ số b:"))
c=float(input("Nhập hệ số c:"))

print("{0}x^2 + {1}x + {2} = 0".format(a,b,c))
if a!=0:
    d=b**2-4*a*c
    if d<0:
        print("Phương trình vô nghiệm")
    elif d==0:
        x = -b/(2*a)
        print("Phương trình có nghiệm kép x1 = x2 =", x)
    else:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        print("Phương trình có nghiệm x1={0} và x2={1}".format(x1,x2))
else:
    m=-c/b
    print("Phương trình có nghiệm x =", m)