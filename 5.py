a=int(input("введите количество людей"))
arr=[]
for i in range(a):
  arr.append(input("введите имя и возраст").split())

a=sorted(arr, key=lambda x: int(x[2]))
print(a[0][0], a[0][1], a[0][2])
