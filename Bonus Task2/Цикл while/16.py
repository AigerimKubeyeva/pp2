n=int(input())
f1=0
f2=1
i=1
result=0
while result<n:
    result=f1+f2
    f1=f2
    f2=result
    i+=1
if n==result:
    print(i)
else:
    print(-1)
