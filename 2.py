a=int(input("введите число"))

def my_div(a):
  max=a
  for i in range(2,a//2+1):
    if a%i==0:
      max=i
  return max
print("наибольший делитель: " + str(my_div(a)))
