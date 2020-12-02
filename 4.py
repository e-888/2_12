a=int(input("введите число"))
b=int(input("введите степень"))

def my_power(a,b):
  if b==0:
    return 1;
  else:
    return a*my_power(a,b-1)
print("результат: " + str(my_power(a,b)))
