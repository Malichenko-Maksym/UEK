a=float(input("The leng of first side is?  "))
while a<=0:
    a=float(input("Give me a corect length  "))
b=float(input("second side is?  "))
while b<=0:
    b=float(input("Give me a corect length  "))
c=float(input("third side is?   "))
while c<=0:
    c=float(input("Give me a corect length  "))
p=(a+b+c)/2
S=(p*(p-a)*(p-b)*(p-c))**0.5
print(f"area is {S}")
input()