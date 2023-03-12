from math import sqrt 
import time 
a=input('print num: ')
b=int(input('print miliseconds: '))
print('Square root of', a, 'after', b, 'miliseconds is......')
time.sleep (b/1000)
print(sqrt(b))