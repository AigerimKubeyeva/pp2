max=0
k=0
n=1
while n!=0:
    n=int(input())
    if n>max:
        max,k=n,1
    elif n==max:
        k+=1
print(k)