import sys

from tasks import add, divide

r1 = add.apply_async((98, 2), propagate= True)


data = [ i for i in range(6)]
 
for num in data:
    divide.apply_async((num, 2), propagate= True)
