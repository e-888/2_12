a=int(input("введите a"))
b=int(input("введите b"))
c=int(input("введите c"))
d=int(input("введите d"))

def min4(a,b,c,d):
  return min(min(a,b),min(c,d))
print ("наименьшее число: "+ str(min4(a,b,c,d)))
