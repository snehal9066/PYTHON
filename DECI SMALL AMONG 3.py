P=int(input("Enter your first number:"))

Q=int(input("Enter your second number:"))

R=int(input("Enter your third number:"))
if P<Q and P<R:
  print(P,"is smallest number")

elif Q<P and Q<R:
  print(Q,"is smallest number")

else:
  print(R,"is smallest number")
