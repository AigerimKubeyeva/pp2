import functools 

print('Enter the number of list items:')
n = int(input())
mylist= []                  
print('Enter', n, 'values:')
for i in range(n):          
    mylist.append(int(input()))
print('Your List:', mylist)
print ('Prod of elements in a list:', functools.reduce(lambda a, b : a * b, mylist)) 