Year=int(input("Enter the year which u want to check:"))
rem1=year%4

if rem1==0:
  rem2=year%4

  if rem2==0:
    print(year,"is a leap year")

  else:
    rem3=rem2%4
    rem4=rem2%100

    if rem3==0 and rem4!=0:
      print(year,"is a leap year")

    else:
      print(year," not a leap year")
else:
  print(year,"not a leap year")
