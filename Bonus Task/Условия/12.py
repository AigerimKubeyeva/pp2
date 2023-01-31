n=int(input()) 
m=int(input()) 
k=int(input()) 

x=n*m

if k<x and (k%m==0 or k%n==0):
    print('YES')
else:
    print('NO')