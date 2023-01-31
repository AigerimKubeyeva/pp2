N=int(input()) 
M=int(input()) 
x=int(input()) 
y=int(input()) 


if N>M: 
    l=min(abs(N-y),y)
    l1=min(abs(M-x),x)
else:
    l=min(abs(M-y),y)
    l1=min(abs(N-x),x)


if l<l1: 
    print(l)
else:
    print(l1)