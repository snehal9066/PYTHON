A=int(input("Enter the lower limit HERE:"))

B=int(input("Enter the upper limit HERE:"))

SUM=0
for i in range(A,B+1):

  PRODUCT=i**2
  if PRODUCT%2==0:

    SUM=SUM-PRODUCT
  else:

    SUM=SUM+PRODUCT
print("Sum of the given series:",SUM)

