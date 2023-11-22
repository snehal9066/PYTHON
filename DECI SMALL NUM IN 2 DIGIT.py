num=int(input("Enter a two digit number:"))

a=num%10

b=num//10
if a==b:
  print("is equal")

if a<b:
  print(a,"is smallest")

if b<a:
  print(b,"is smallest")

