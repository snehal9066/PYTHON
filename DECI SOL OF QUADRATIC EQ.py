a=int(input("Enter the coefficient of x2:"))

b=int(input("Enter the coefficient of x:"))

c=int(input("Enter the constant term :"))

d=(b**2)-(4*a*c)
if d>=0:
  if d>0:
    print("The quadratic equation have two real solutions")

  if d==0:
    print("The quadratic equation has two equal solutions")

if d<0:
  print("The quadratic equation has no real solutions")

