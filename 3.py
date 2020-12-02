a=int(input("введите a"))
b=int(input("введите b"))

def sum(a,b):
  if b==1:
    if a==1:
      return 2
    else:
      return 1+sum(a-1,b)
  else:
    return 1+sum(a,b-1)
print("сумма: " + str(sum(a,b)))
