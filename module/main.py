from math import pi, pow 
from calculate import  add,multi


r = 3
area =   pi * pow(r,2)
print(area)


add(5,7)
product = multi(12,2)
print(product)

if product % 2 == 0:
    print("the number is even")
else:
    print("odd")