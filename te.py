left = 1 
right = 15 
x = input("введём число: ")
x = int(x)

if x >= left and x <= right:
    print("число не вышло за границу")
else: 
    print("число вышло за границу")