w=float(input("Your weight is?(in KG)  "))
while w<=0:
    w=float(input("Give me a corect weight   "))
h=float(input("Your height is?(in CM)  "))
while h<=0:
   h=float(input("Give me a corect heigth  "))
i=w/h/h*10000
print(f"BMI index: {i}")
input()