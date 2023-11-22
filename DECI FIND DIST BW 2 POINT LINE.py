A=int(input("Enter first point:"))
B=int(input("Enter second point: "))

if A==B:
  print("Distance is 0")

else:
  X=((B-A)**2)**(1/2)
  print("Distance between two points is==",X)
