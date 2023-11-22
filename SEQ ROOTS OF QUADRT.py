a=int(input("Enter coefficient of x2:"))

b=int(input("Enter coefficient of x:"))

c=int(input("Enter constant term:"))

D=b**2-(4*a*c)

r1=(b-(D)**(1/2))/2*a
r2=(b+(D)**(1/2))/2*a

print("ROOTS ARE:\n",r1,"\n",r2)
