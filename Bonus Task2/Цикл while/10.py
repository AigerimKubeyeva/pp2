x=int(input())
max=x
index=0
pos=0
while x!=0:
    x=int(input())
    index+=1
    if x>max:
        max=x
        pos=index
print(pos)